ARG TARGET_VERSION

FROM python:3.6-alpine

WORKDIR /app

RUN pip install setuptools wheel twine

COPY post-release-data.py ../
COPY sceptre_dot ./sceptre_dot
COPY release.sh setup.py ./

CMD ["./release.sh"]
