import multiprocessing

bind = "0.0.0.0:10398"
workers = multiprocessing.cpu_count() * 2 + 1