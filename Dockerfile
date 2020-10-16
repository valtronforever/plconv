FROM ubuntu:18.04
USER root
ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y build-essential debhelper devscripts equivs python3-venv python3-dev python3-setuptools python3-wheel python3-all python-virtualenv
RUN apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev
RUN apt-get install -y python3-stdeb dh-virtualenv libatlas-base-dev libblas-dev
RUN apt-get install -y git
ADD plconv/requirements.txt /home/
RUN git clone https://github.com/valtronforever/plconv.git /home/plconv
RUN cd /home/plconv && virtualenv -p python3 .env
RUN /home/plconv/.env/bin/pip install -r /home/plconv/plconv/requirements.txt
RUN /home/plconv/.env/bin/pip install make-deb

