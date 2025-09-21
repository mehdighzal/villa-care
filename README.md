# VillaCare - Luxury Villa Service Platform

VillaCare is a premium Django-based web application designed for luxury villa owners who demand the highest quality property care and management services. The platform features an elegant black and gold design theme that reflects the luxury and sophistication of the target market.

## Features

### 🏠 **Website Structure**
- **Header**: VillaCare logo with navigation menu (Home, About, Services, Packages, Contact, Reviews)
- **Hero Section**: Eye-catching carousel with high-quality villa images
- **About Us**: Company description and philosophy
- **Services**: Comprehensive list of villa care services
- **Packages**: Elegant black & gold package cards with subscription options
- **Contact Form**: Professional contact form with name, email, and message fields
- **Reviews**: Customer testimonials with star ratings and review submission form
- **Footer**: Company information, quick links, and search functionality

### 🎨 **Design Theme**
- **Colors**: Black and gold luxury theme
- **Typography**: Modern, elegant fonts
- **Layout**: Responsive design with Bootstrap 5
- **Animations**: Smooth transitions and hover effects
- **Icons**: Font Awesome icons for enhanced visual appeal

### 🛠 **Technical Features**
- **Django Framework**: Robust backend with admin panel
- **User Authentication**: Complete login/register system with user profiles
- **Villa Reporting System**: Users can create and track villa care reports
- **Models**: Contact, Review, Package, UserProfile, and VillaReport models
- **Forms**: Django forms with validation and styling
- **Admin Panel**: Full CRUD operations for managing content and user reports
- **Responsive Design**: Mobile-friendly interface
- **AJAX Forms**: Smooth form submissions without page reloads
- **User Dashboard**: Personalized dashboard with statistics and recent reports

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd villa-care
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data**
   ```bash
   python manage.py populate_data
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Test User Login: username: `testuser`, password: `testpass123`

## Models

### Contact Model
- `name`: Customer name
- `email`: Customer email address
- `message`: Contact message
- `created_at`: Timestamp of submission

### Review Model
- `name`: Reviewer name
- `rating`: Star rating (1-5)
- `comment`: Review text
- `is_approved`: Admin approval status
- `created_at`: Timestamp of submission

### Package Model
- `name`: Package name
- `package_type`: Weekly, Monthly, or Yearly
- `description`: Package description
- `price`: Package price
- `features`: List of package features
- `is_featured`: Featured package flag
- `created_at`: Creation timestamp

### UserProfile Model
- `user`: One-to-one relationship with Django User
- `phone`: User's phone number
- `address`: User's address
- `villa_address`: Villa property address
- `villa_type`: Type of villa (Modern, Traditional, etc.)
- `subscription_package`: Associated service package
- `created_at`: Profile creation timestamp

### VillaReport Model
- `user`: Foreign key to User
- `report_type`: Type of report (maintenance, cleaning, security, etc.)
- `priority`: Priority level (low, medium, high, urgent)
- `title`: Report title
- `description`: Detailed description
- `location`: Specific location in villa
- `status`: Current status (pending, in_progress, completed, cancelled)
- `admin_notes`: Internal notes for staff
- `scheduled_date`: Scheduled service date
- `completed_date`: Completion timestamp

## Admin Panel

The admin panel provides full management capabilities:

- **Contact Management**: View and manage customer inquiries
- **Review Management**: Approve/reject customer reviews
- **Package Management**: Create and manage service packages
- **User Profile Management**: View and manage user profiles
- **Villa Report Management**: Track and manage villa care reports
- **User Management**: Manage admin users and permissions

## User Features

### Authentication System
- **User Registration**: Create new accounts with email verification
- **User Login**: Secure authentication with session management
- **User Profiles**: Manage personal and villa information
- **Password Security**: Django's built-in password validation

### Villa Reporting System
- **Admin-Only Report Creation**: Only administrators can create villa reports for clients
- **Client Commenting**: Users can comment on their assigned reports
- **Track Status**: Monitor report progress (pending, in_progress, completed)
- **Priority Levels**: Set urgency levels (low, medium, high, urgent)
- **Location Tracking**: Specify exact villa locations for services
- **Two-Way Communication**: Admin and client comments for seamless communication

### User Dashboard
- **Statistics Overview**: View total, pending, and completed reports
- **Recent Reports**: Quick access to latest assigned reports
- **Quick Actions**: Fast navigation to view reports and update profile
- **Profile Management**: Update personal and villa information

### Admin Dashboard
- **Report Management**: Create, edit, and manage villa reports for clients
- **Client Assignment**: Assign reports to specific users
- **Status Updates**: Update report status and add admin notes
- **Comment System**: Add admin comments and view client feedback
- **Statistics Overview**: View all reports, pending, in-progress, and completed
- **Recent Activity**: Monitor recent reports and comments

## Customization

### Adding New Services
1. Access the admin panel
2. Navigate to "Packages"
3. Add new package with appropriate details
4. Set features using newline-separated format

### Managing Villa Reports
1. **Admin Dashboard**: Access the admin dashboard at `/admin-dashboard/`
2. **Create Reports**: Use "Create Report" to assign reports to clients
3. **Edit Reports**: Update report status, priority, and details
4. **Add Comments**: Communicate with clients through the comment system
5. **Monitor Activity**: View recent reports and comments

### Admin Access
- **Admin Dashboard**: http://127.0.0.1:8000/admin-dashboard/
- **Create Report**: http://127.0.0.1:8000/admin/create-report/
- **Django Admin**: http://127.0.0.1:8000/admin/
- **Admin Login**: Use the superuser account created during setup

### Modifying Design
- **CSS**: Edit `static/css/style.css` for styling changes
- **JavaScript**: Modify `static/js/main.js` for functionality
- **Templates**: Update `templates/main/home.html` for layout changes

### Adding New Features
- Create new models in `main/models.py`
- Add corresponding forms in `main/forms.py`
- Update views in `main/views.py`
- Create new templates as needed

## File Structure

```
villa-care/
├── villacare/           # Django project settings
├── main/               # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── admin.py        # Admin configuration
│   ├── urls.py         # URL patterns
│   └── management/     # Management commands
├── templates/          # HTML templates
│   └── main/
│       └── home.html   # Main homepage template
├── static/             # Static files
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   ├── js/
│   │   └── main.js     # JavaScript functionality
│   └── images/         # Image assets
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Technologies Used

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome
- **Database**: SQLite (development)
- **Images**: Unsplash (placeholder images)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please contact:
- Email: info@villacare.com
- Phone: +1 (555) 123-4567

---

**VillaCare** - Where luxury meets excellence in villa care services.
