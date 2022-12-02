# Ordinal Regression to Predict NBA Draft Number From Years 2020 to 2022

## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Usage](#usage)

## Introduction
With so many world-class basketball players, how do NBA teams decide who to draft? By gathering the recent years NBA draft data, I created visualizations on a dashboard in Power BI displaying the differences between the first and second round picks. Based on a players pre-NBA career stats, I deployed an ordinal regression model in Python to predict the draft number and round. Run the model by using the Docker image that I created. 

## Technologies
<img align="left" alt="Python" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" />
<img align="left" alt="PowerBI" width="30px" style="padding-right:10px;" src="https://www.vectorlogo.zone/logos/microsoft_powerbi/microsoft_powerbi-icon.svg" />
<img align="left" alt="Docker" width="30px" style="padding-right:10px;" src="https://cdn.worldvectorlogo.com/logos/docker.svg" /> 
<br />

## Usage

[Click to View Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjVjMzgxMWQtZDE4Ni00ZmFkLTk3ZjEtYzNkY2Y3ZmM2ODBkIiwidCI6IjI2ZThiMDQ4LTA3OTktNGI2Yy04NjA5LTZlMWU5NDQ3YmViNyJ9&pageName=ReportSection7358636ad12277a1b663)

To replicate and run the Python script containing the model:
* First download the files via the command line in the terminal
  ```sh
  git clone https://github.com/bensonouyang/Draft-Prediction.git
  ```
* Once the files are downloaded, next build the Docker image
  ```sh
  docker build -f Dockerfile -t docker_draft_analysis
  ```
* After the Docker image is built, now run the Docker image
  ```sh
  docker run -ti docker_draft_analysis /bin/bash
  ```
* Can now activate new environment
  ```sh
  source activate draft
  ```
* Change to the directory containing the files
  ```sh
  cd src
  ```
* Run the Python script
  ```sh
  python 04-Predictions.py
  ```



