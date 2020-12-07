"""In this exercise, I was given task based a real-world situation where a radiologist's worklist needs to be prioritised.
In this scenario, I had a radiologist who works in a very busy emergency department in a major city. They often see a >100
of emergency images that need to be read every day, and there is no prioritisation around those images because they come in
through the emergency department, so everything is marked as "urgent."

In the current setting, radiologists read these images in a first-in-first-out queue, where all images are simply
read in the order that they come in. From a clinical perspective, I knew that some urgent cases are truly more urgent
than others. In a hypthetical situation I knew from my research in interviewing emergency doctors and radiologists, I
have identified that two of the most urgent types of findings on an image are a cerebral hemorrhage (brain bleed) and an aortic dissection.
Both of these medical emergencies are etiological factor that results a patient death within minutes, but they can only be detected on imaging.
Therefore it is impertive the patients are priortised based on the severity of the case of which requires l urgent
medical attention and the images provided were prioritised.

In addition, deep learning was used to create two classification algorithms, one for the detection of brain bleeds on head CT images,
and the other for the detection of aortic dissection based on chest x-ray images. The algoroithgms were then intograted into the radiologist's
workflow so that they are most helpful clinically.

In this exercise I was given the following:

- A list of images that have come in through the ED in order of patient arrival;
- Probabilities of 'brain bleed' for each image, as determined by the developed deep learning algorithms (DDLA) and ;
- Probabilities of 'aortic dissection' for each image, as determined the DDLA.

The following asked to be completed:

- To calculate the amount of time it will take before each image is read by the radiologist, given the patient arrival queue,
  assuming each image takes 6 minutes to read
- To implement a heuristic which uses cross-sectional probablabic algorathim returned by the DDLA to re-order the priority read list, assuming that brain bleeds and aortic dissections are equally urgent
- To calculate the time delta for each image between the initial and the re-ordered priority reads


I also was given the optional opportunity to answer the following questions based on my reprioritisation:

- Comment on whether if my algorithm's goal was to have brain bleeds read 30 minutes faster, how did it do?
- Comment on whether if my algorithm's goal was to have aortic dissections read 15 minutes faster, how did it do?
- Comment on whethere if there was any cases where my algorithm made it worse for patients who needed an ASAP medical attention? Could anything have been done about this?"""