from DE_Assigment.ploting import *

# Costs:
# ______________________________
steps_count = 1000
X = 0

glob_err_start = 10
glob_err_end = 100
# ______________________________


# Plotting graphs for each task:
plot_methods(steps_count, X)
plot_local_error(steps_count, X)
plot_global_error(glob_err_start, glob_err_end, X)
