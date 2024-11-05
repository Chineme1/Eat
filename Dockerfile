FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -v --trusted-host pypi.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip \
    libxss1 \
    libappindicator3-1 \
    libgconf-2-4 \
    libxi6 \
    libxrandr2 \
    libxcomposite1 \
    libxcursor1 \
    libasound2 \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libxshmfence1 \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && apt-get clean

#114.0.5735
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip


# Check installed versions
RUN google-chrome --version && chromedriver --version


# Expose the port Flask is set to run on
EXPOSE 5000

CMD ["python", "main.py"]