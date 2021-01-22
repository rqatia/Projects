This model mimics the random arrival of patients at an emergency department (ED). The patients are assessed as being low, medium or high priority. Higher priority patients are always selected next (but do not displace lower priority patients already being seen by a doctor).

This model requires some understanding of object-oriented programming in Python.

There are four classes of object in the model:

1) A global variables class. These are stored directly, and may edited, in the class definition.

2) A model class. There is one instance of this class created. This holds the SimPy model.

3) A patient class. A new instance of this class is triggered with each patient arrival. The patient object holds all relevant information about individual patients (such as their priority level).

4) A resources class. There is one instance of this class created which holds the doctors (if other resources were required they could also be held here).

There is a warm-up period before the auditing of results starts.