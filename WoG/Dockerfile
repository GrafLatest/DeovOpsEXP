FROM python
WORKDIR ./app/
COPY *.py /app/
COPY Scores.txt /app/
COPY prereq.txt prereq.txt
RUN pip install --upgrade pip
RUN pip install -r prereq.txt
EXPOSE 8585
CMD python3 main_game.py