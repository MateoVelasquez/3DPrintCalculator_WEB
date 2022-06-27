FROM continuumio/miniconda3

WORKDIR /3DPrintCalculator_WEB


# Create the environment.
COPY environment.yml .
RUN conda env create -f environment.yml

COPY . /3DPrintCalculator_WEB

# Make RUN commands use the new environment:
RUN echo "conda activate cal_env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "from flask_migrate import Migrate"

# Puerto de escucha
EXPOSE 7001

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cal_env", "python", "run.py"]