#
# gen_jupyter_passwd.py
# =============================================================================
from notebook.auth import passwd


passwd()
# You can then add the hashed password to your jupyter_notebook_config.py
# The default location for this file jupyter_notebook_config.py is in your 
# Jupyter folder in your home directory, ~/.jupyter
# ```
# c.NotebookApp.password = \
#              u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
# ```
