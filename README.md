# pidactic-kidney
A one dimensional random walk simulation that uses python multiprocessing.

This version uses multiprocessing.map. On a 4 thread i7 laptop it runs in less then 0.02 seconds. The older version using multiprocessing.Process (With a global Value and a Lock) took 3 seconds. 
