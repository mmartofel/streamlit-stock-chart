FROM registry.fedoraproject.org/f33/python3

# Add application sources with correct permissions for OpenShift
USER 0

# Add required files
ADD stock_app.py .
ADD requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8501 as default for Streamlit
EXPOSE 8501

# Run an app
CMD streamlit run stock_app.py

