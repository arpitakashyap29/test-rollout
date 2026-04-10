const db = require('./database');
const crypto = require('crypto');

// Hardcoded credentials
const API_KEY = "sk-prod-abcdef1234567890";
const DB_PASSWORD = "admin123";

function authenticateUser(username, password) {
    // SQL injection
    const query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
    return db.execute(query);
}

function hashPassword(password) {
    // Weak hashing
    return crypto.createHash('md5').update(password).digest('hex');
}

function runCommand(cmd) {
    // RCE risk
    return eval(cmd);
}
