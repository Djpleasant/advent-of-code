# syntax=docker/dockerfile:1
# Define image target.
ARG IMAGE_REGISTRY=docker.io
ARG IMAGE_NAMESPACE=library
ARG IMAGE_TAG=python
ARG IMAGE_VERSION=3.10-alpine
ARG IMAGE_PATH=${IMAGE_REGISTRY}/${IMAGE_NAMESPACE}/${IMAGE_TAG}:${IMAGE_VERSION}

FROM ${IMAGE_PATH}

ENV LC_ALL=C.UTF-8

# ---------#
# Globals #
# ---------#
ARG DEVELOPER_DIR=/usr/src/app

# -----------#
# OS setup. #
# -----------#
# Update operating system.
RUN apk update && \
    apk upgrade && \
    apk cache purge

# Add additional tools.
RUN apk add curl \
    && apk cache purge

# Instal 'uv'.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Create directory to map project into.
RUN mkdir --parents ${DEVELOPER_DIR}

# ------#
# Main #
# ------#
WORKDIR ${DEVELOPER_DIR}
ENTRYPOINT [ "/bin/sh" ]
CMD [ ]
