FROM continuumio/miniconda
RUN conda install -yq conda-build
COPY . /src/conda-nodejs
WORKDIR /src/conda-nodejs
RUN conda build conda.recipe
