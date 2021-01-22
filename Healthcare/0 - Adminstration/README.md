  
# Prioritised Replay Noisy Duelling Double Deep Q Learning - A simple hospital model  
  
In this example I develop a Noisy Duelling Double Q Learning algorithim and add a *Prioritised Replay* memory. Using this type of memory, state/actions that have the highest loss (error) when training our policy network are sampled more frequently than state/actions that have low loss.   
  
## A simple hospital simulation model  
  
This is an example of a simple hospital bed model where a Reinforcement learning (RL) agent has to learn how to manage the bed stock:  
  
 • Default arrivals = 50/day • Weekend arrival numbers are 50% average arrival numbers • Weekday arrival numbers are 120% average arrival numbers • Distribution of inter-arrival time is inverse exponential • Average length of stay is 7 days (default) • Distribution of length of stay is inverse exponential • The RL agent may request a change in bed numbers once a day (default) • The allowed bed change requests are -20, -10, 0, 10, 20 • Bed changes take 2 days to occur (default) • The RL agent receives a reward at each action based on the number of free beds or number of patients without a bed • The simulation is loaded with the average number of patients present  The RL agent must learn to maximise the long term reward (return). The maximum reward = 0, so the agent is learning to minimise the loss for each unoccupied bed or patient without bed.  
  
## Reinforcement learning introduction  
  
### RL involves:  
* Trial and error search  
* Receiving and maximising reward (often delayed)  
* Linking state -> action -> reward  
* Must be able to sense something of their environment  
* Involves uncertainty in sensing and linking action to reward  
* Learning -> improved choice of actions over time  
* All models find a way to balance best predicted action vs. exploration  
  
### Elements of RL  
* *Environment*: all observable and unobservable information relevant to us  
* *Observation*: sensing the environment  
* *State*: the perceived (or perceivable) environment   
* *Agent*: senses environment, decides on action, receives and monitors rewards  
* *Action*: may be discrete (e.g. turn left) or continuous (accelerator pedal)  
* *Policy* (how to link state to action; often based on probabilities)  
* *Reward signal*: aim is to accumulate maximum reward over time  
* *Value function* of a state: prediction of likely/possible long-term reward  
* *Q*: prediction of likely/possible long-term reward of an *action*  
* *Advantage*: The difference in Q between actions in a given state (sums to zero for all actions)  
* *Model* (optional): a simulation of the environment  
  
### Types of model  
  
* *Model-based*: have model of environment (e.g. a board game)  
* *Model-free*: used when environment not fully known  
* *Policy-based*: identify best policy directly  
* *Value-based*: estimate value of a decision  
* *Off-policy*: can learn from historic data from other agent  
* *On-policy*: requires active learning from current decisions  
  
  
## Duelling Deep Q Networks for Reinforcement Learning  
  
Q = The expected future rewards discounted over time. This is what we are trying to maximise.  
  
The aim is to teach a network to take the current state observations and recommend the action with greatest Q.  
  
Duelling is very similar to Double DQN, except that the policy net splits into two. One component reduces to a single value, which will model the state *value*. The other component models the *advantage*, the difference in Q between different actions (the mean value is subtracted from all values, so that the advtantage always sums to zero). These are aggregated to produce Q for each action.   
  
  ![](https://github.com/MichaelAllen1966/learninghospital/raw/9c67c96e4d027a20ffc862ec26f6690844e159be/images/duelling_dqn.png) 
  
Q is learned through the Bellman equation, where the Q of any state and action is the immediate reward achieved + the discounted maximum Q value (the best action taken) of next best action, where gamma is the discount rate.  
  
$$Q(s,a)=r + \gamma.maxQ(s',a')$$  
  
## Key DQN components  
  
![](https://github.com/MichaelAllen1966/learninghospital/raw/9c67c96e4d027a20ffc862ec26f6690844e159be/images/dqn_components.png)
  
  
## General method for Q learning:  
  
Overall aim is to create a neural network that predicts Q. Improvement comes from improved accuracy in predicting 'current' understood Q, and in revealing more about Q as knowledge is gained (some rewards only discovered after time).  
  
![](https://github.com/MichaelAllen1966/learninghospital/raw/9c67c96e4d027a20ffc862ec26f6690844e159be/images/dqn_process.png)
      
Target networks are used to stabilise models, and are only updated at intervals. Changes to Q values may lead to changes in closely related states (i.e. states close to the one we are in at the time) and as the network tries to correct for errors it can become unstable and suddenly lose signficiant performance. Target networks (e.g. to assess Q) are updated only infrequently (or gradually), so do not have this instability problem.  
  
## Training networks  
  
Double DQN contains two networks. This ammendment, from simple DQN, is to decouple training of Q for current state and target Q derived from next state which are closely correlated when comparing input features.  
  
The *policy network* is used to select action (action with best predicted Q) when playing the game.  
  
When training, the predicted best *action* (best predicted Q) is taken from the *policy network*, but the *policy network* is updated using the predicted Q value of the next state from the *target network* (which is updated from the policy network less frequently). So, when training, the action is selected using Q values from the *policy network*, but the the *policy network* is updated to better predict the Q value of that action from the *target network*. The *policy network* is copied across to the *target network* every *n* steps (e.g. 1000).  
  
![](https://github.com/MichaelAllen1966/learninghospital/raw/9c67c96e4d027a20ffc862ec26f6690844e159be/images/dqn_training.png)
## Noisy layers  
Noisy layers are an alternative to epsilon-greedy exploration (here, we leave the epsilon-greedy code in the model, but set it to reduce to zero immediately after the period of fully random action choice).  
  
For every weight in the layer we have a random value that we draw from the normal distribution. This random value is used to add noise to the output. The parameters for the extent of noise for each weight, sigma, are stored within the layer and get trained as part of the standard back-propogation.  
  
A modification to normal nosiy layers is to use layers with ‘factorized gaussian noise’. This reduces the number of random numbers to be sampled (so is less computationally expensive). There are two random vectors, one with the size of the input, and the other with the size of the output. A random matrix is created by calculating the outer product of the two vectors.  
  
## Prioritised replay  
  
In standard DQN samples are taken randomly from the memory (replay buffer). In *prioritised replay* samples are taken in proportion to their loss when training the network; where the network has the greatest error in predicting the target valur of a state/action, then those samples will be sampled more frequently (which will reduce the error in the network until the sample is not prioritised). In other words, the training focuses more heavenly on samples it gets most wrong, and spends less time training on samples that it can acurately predict already.  
  
This priority may also be used as a weight for training the network, but this i snot implemented here; we use loss just for sampling.  
  
When we use the loss for priority we add a small value (1e-5) t the loss. This avoids any sample having zero priority (and never having a chance of being sampled). For frequency of sampling we also raise the loss to the power of 'alpha' (default value of 0.6). Smaller values of alpha will compress the differences between samples, making the priority weighting less significant in the frequency of sampling.  
  
## References  
  
Double DQN:   
van Hasselt H, Guez A, Silver D. (2015) Deep Reinforcement Learning with Double Q-learning. arXiv:150906461 http://arxiv.org/abs/1509.06461  
  
Duelling DDQN:  
Wang Z, Schaul T, Hessel M, et al. (2016) Dueling Network Architectures for Deep Reinforcement Learning. arXiv:151106581 http://arxiv.org/abs/1511.06581  
  
Noisy networks:  
Fortunato M, Azar MG, Piot B, et al. (2019) Noisy Networks for Exploration. arXiv:170610295 http://arxiv.org/abs/1706.10295  
  
Prioritised replay:  
Schaul T, Quan J, Antonoglou I, et al (2016). Prioritized Experience Replay. arXiv:151105952 http://arxiv.org/abs/1511.05952  
  
Code for the nosiy layers comes from:  
  
Lapan, M. (2020). Deep Reinforcement Learning Hands-On: Apply modern RL methods to practical problems of chatbots, robotics, discrete optimization, web automation, and more, 2nd Edition. Packt Publishing.