CREATE TABLE users (
    user_id VARCHAR(20) PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,  
    email VARCHAR(100) NOT NULL,
    profile_picture VARCHAR(255),
    role VARCHAR(50) NOT NULL
);