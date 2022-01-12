FROM python:3.9

# Security baby
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_ID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --create-home --uid $USER_UID --gid $USER_GID $USERNAME
WORKDIR /home/$USERNAME

# Don't compile to Python bytecode (.pyc files)
ENV PYTHONWRITEBYTECODE 1

# Force python output to stdout/stderr without buffering
ENV PYTHONBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]
