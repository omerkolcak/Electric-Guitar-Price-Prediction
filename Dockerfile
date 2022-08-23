FROM python:3.9
COPY /application /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD "streamlit run /app/main.py"
# ENTRYPOINT ["streamlit","run"]
# CMD ["main.py"]
