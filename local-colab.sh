# install and enable extension before running
# pip install jupyter_http_over_ws
# jupyter serverextension enable --py jupyter_http_over_ws
# --------------------------------------------------------
pipenv run jupyter notebook \
  --NotebookApp.token='adahdskdhquiwh' \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --no-browser \
  --NotebookApp.port_retries=0
