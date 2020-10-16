FROM ubuntu:18.04
USER root
RUN apt-get update && apt-get install -y build-essential debhelper devscripts equivs python3-venv python3-dev python3-setuptools python3-wheel
RUN apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev
RUN apt-get install -y git
RUN git clone https://github.com/valtronforever/plconv.git /home/plconv
RUN cd /home/plconv && virtualenv -p python3 .env
RUN /home/plconv/.env/bin/pip install -r /home/plconv/plconv/requirements.txt
