from eztv_api import EztvAPI
import subprocess
test_api=EztvAPI().tv_show('Game of Thrones')
print subprocess.check_output('transmission-remote -a '+test_api.episode(1,3), shell=True)
