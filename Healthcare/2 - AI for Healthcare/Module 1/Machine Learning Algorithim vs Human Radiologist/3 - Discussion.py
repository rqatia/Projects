"""
Reflection:
In the exercise I assessed performances of a human as well as of an
algorithm against a 'perfect labeler' and also against each other.
Does accuracy seem like the appropriate statistic to use when evaluating 
these labels? Why or why not?


Given that there are so many fewer cancer cases than benign cases, accuracy 
would not be a good statistic to use. A human or an algorithm could label
all of the cancer cases as benign and still achieve an accuracy of over 80%.

Higher levels of false negatives aren't great ever in clinical settings, but 
they have less of an impact on the patient if we know that there will be a second
reader (i.e. our algorithm reads an image first, and then the label is confirmed 
by a radiologist). This also would only be appropriate if there wasn't a time-sensitive
aspect to making the diagnosis. It seems more acceptable to have a high level of false
positives in a situation as we saw in the previous exercise, where our algorithm was
being used to prioritize emergency reads, in which case we would want to be somewhat
liberal.

Changing the threshold on the algorithm performance changed the FP and FN rates,
one at the expense of the other.

The algorithm's true positive rate increased when using the same threshold and
comparing it to the human instead of the perfect labeler. This means that without
the true ground truth of diagnoses in an image, we may never be able to 100% accurately
assess our algorithm, and its results may be inflated based on the quality of the radiologist
labels that we use in comparing our outputs.

"""
