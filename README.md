
# Single Window Clearance Portal

## Overview
The Single Window Clearance Portal is designed to streamline the request process between college clubs and the student gymkhana. This portal allows clubs to generate various types of requests—monetary or non-monetary—and send them to the relevant authorities for approval through an organized chain of command. Both the **Club Faculty Advisor (FA)** and the **Society FA** have the ability to accept the requests. Additionally, all the information related to the requests will be stored and made accessible to the **Dean** for oversight.

## Key Features
- **Request Generation**: Clubs can submit requests through a user-friendly interface. Requests can be monetary (e.g., budget approvals, financial reimbursements) or non-monetary (e.g., event permissions, resource allocation).
  
- **Chain of Command**: Requests are routed to the appropriate authority based on the type and content of the request:
  - **Club FA**: First level of approval.
  - **Society FA**: Second level of approval, after Club FA.
  - **Dean**: Has the authority to view all requests and their status for supervision purposes.

- **Request Tracking**: Each request is tracked in real-time. Clubs can view the status of their requests (Pending, Approved, Rejected, etc.) at any time.

- **Audit Logs**: All actions taken on the requests are logged and stored for future reference. The Dean can access these logs for auditing purposes.

- **User Roles**: 
  - **Club User**: Can generate requests and view request statuses.
  - **Club FA**: Can view and approve/reject requests from their club.
  - **Society FA**: Can view and approve/reject requests routed from the Club FA.
  - **Dean**: Can view all requests and monitor the overall workflow.

## Technology Stack
- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Bootstrap for styling and responsiveness

- **Backend**: 
  - Flask for handling requests and routing.
  
- **Database**:
  - MySQL for storing requests, user data, and approval history.
  
- **Authentication**: 
  - OAuth authentication for secure login and access control.

- **API Integration**:
  - REST APIs for fetching and updating request status.

## Database Schema
### Tables
1. **Users Table**: Stores details of club members, FAs, and Dean.
   - `user_id`: Primary key.
   - `name`, `email`, `role` (club member, FA, society FA, dean).

2. **Requests Table**: Stores the requests generated by clubs.
   - `request_id`: Primary key.
   - `club_id`: Foreign key (related to the club).
   - `request_type`: Monetary/Non-monetary.
   - `description`: Details of the request.
   - `status`: Pending/Approved/Rejected.
   - `created_at`: Timestamp for request creation.

3. **Approvals Table**: Tracks the approval process for each request.
   - `approval_id`: Primary key.
   - `request_id`: Foreign key (related to request).
   - `approver_id`: Foreign key (related to the approver, i.e., FA/Society FA).
   - `approval_status`: Approved/Rejected.
   - `updated_at`: Timestamp for when the approval decision was made.

## Usage

### Club Member Workflow:
1. Log in to the portal using your credentials.
2. Navigate to the **Create Request** section.
3. Fill out the request form with all necessary details (type, description, attachments if necessary).
4. Submit the request for approval.

### Club FA Workflow:
1. Log in and navigate to the **Requests** section.
2. View pending requests from clubs under your supervision.
3. Approve or reject the request and provide comments if necessary.

### Society FA Workflow:
1. Log in and navigate to the **Requests** section.
2. View requests forwarded by the Club FA.
3. Approve or reject the requests accordingly.

### Dean Workflow:
1. Log in and navigate to the **Audit Logs** or **Requests Overview** section.
2. Monitor all requests and approvals in the system.
3. View approval trends and club activity over time.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/single-window-clearance-portal.git
    ```

2. **Install dependencies** (for Node.js/Express setup):
    ```bash
    cd single-window-clearance-portal
    npm install
    ```

3. **Configure the database**:
   - Set up a MySQL/PostgreSQL database.
   - Update the connection details in the configuration file.

4. **Run the application**:
    ```bash
    npm start
    ```

5. **Access the portal** at `http://localhost:3000` (or your configured port).

## Future Enhancements
- **Email Notifications**: Automatically send email alerts to FAs and club members when requests are approved or rejected.
- **Analytics Dashboard**: Provide insights on the types and frequency of requests, processing times, etc., to help optimize workflows.
- **Mobile Application**: Build a mobile app for easier access to the portal.

## Contributing
We welcome contributions to this project. Please fork the repository, create a new branch for your feature or bugfix, and submit a pull request!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
