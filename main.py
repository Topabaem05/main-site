#from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs
from save import save_to_file

sof_jobs = get_sof_jobs()
#indeed_jobs = get_indeed_jobs()
jobs = sof_jobs
save_to_file(jobs)