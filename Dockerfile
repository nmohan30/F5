FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY search.py /src/search.py
COPY content.py /src/content.py


EXPOSE  8000
CMD ["python", "/src/content.py", "-p 8000"]
CMD ["python", "/src/search.py", "-p 8000"]
