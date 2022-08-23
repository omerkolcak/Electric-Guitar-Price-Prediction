FROM python:3.9
COPY /application /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD streamlit run main.py --server.port 5500
# ENTRYPOINT ["streamlit","run"]
# CMD ["main.py"]
