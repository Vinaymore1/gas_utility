# 🔥 Gas Utility Customer Service Platform

## 🌟 Project Overview

A cutting-edge web application designed to revolutionize customer service in the gas utility industry, leveraging modern web technologies to enhance user experience, operational efficiency, and communication.

## 🚀 Key Features

### 💡 Advanced User Management
- **Secure Authentication**: Implemented JWT-based authentication with role-based access control
- **Multi-tier User Roles**: 
  - Customers: Submit and track service requests
  - Support Staff: Manage and resolve customer issues
  - Administrators: Full system oversight and configuration

### 🛠 Intelligent Service Request Management
- **Comprehensive Request Handling**
  - Online submission with detailed categorization
  - Real-time status tracking
  - Seamless file attachment support
- **Communication Workflow**
  - Integrated commenting system
  - Detailed request history tracking
  - Automated email notifications

### 🔒 Robust Security Features
- **Rate Limiting**: Protect against API abuse
- **Secure Authentication**: JWT-based with role-based permissions
- **Data Integrity**: Comprehensive input validation and error handling

### 📊 Powerful Administrative Tools
- **Intuitive Dashboard**
  - Advanced search and filtering capabilities
  - Real-time request management
  - Comprehensive reporting and analytics

## 🛠 Technical Stack

### Backend
- **Language**: Python 3.8+
- **Framework**: Django 4.2
- **Authentication**: JSON Web Tokens (JWT)
- **API Documentation**: drf-spectacular
- **Database**: PostgreSQL

### Key Technologies
- Django Rest Framework
- Celery (for asynchronous tasks)
- Docker (containerization)
- Swagger/OpenAPI for API documentation

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip
- virtualenv

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/gas-utility-crm.git
   cd gas-utility-crm
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## 🔍 API Endpoints

### Authentication
- `POST /api/accounts/register/` - User Registration
- `POST /api/accounts/token/` - Login & Token Generation
- `POST /api/accounts/logout/` - User Logout

### Service Requests
- `GET /api/service-requests/` - List Requests
- `POST /api/service-requests/` - Create Request
- `GET /api/service-requests/{id}/` - Retrieve Specific Request
- `PUT /api/service-requests/{id}/` - Update Request

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

- **Your Name**
- **Email**: vinayvilasmore@gmail.com
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/vinay-more-6ba17322b/)
- **GitHub**: [Your GitHub](https://github.com/vinaymore1)

---

**Built with ❤️ for modern utility customer service**
