import streamlit as st
import pandas as pd
from io import BytesIO
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Enhanced Code Viewer with Demo Examples",
    layout="wide"
)

# --- DEMO EXAMPLES ---
DEMO_EXAMPLES = {
    "1": {
        "title": "Newsletter Template - Real Estate Weekly",
        "category": "Newsletter",
        "downloadable": True,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Weekly Newsletter</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; background: #f4f4f4; }
        .container { max-width: 600px; margin: 0 auto; background: white; }
        .header { background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 30px; text-align: center; }
        .header h1 { font-size: 28px; margin-bottom: 10px; }
        .header p { font-size: 16px; opacity: 0.9; }
        .content { padding: 30px; }
        .property-card { border: 1px solid #ddd; border-radius: 8px; margin: 20px 0; overflow: hidden; }
        .property-image { width: 100%; height: 200px; background: linear-gradient(45deg, #3498db, #2ecc71); display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; }
        .property-info { padding: 20px; }
        .property-price { font-size: 24px; font-weight: bold; color: #e74c3c; margin-bottom: 10px; }
        .property-details { color: #666; margin-bottom: 15px; }
        .cta-button { background: #3498db; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 10px; }
        .footer { background: #2c3e50; color: white; padding: 20px; text-align: center; }
        .download-btn { position: fixed; top: 10px; right: 10px; background: #e74c3c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <button class="download-btn" onclick="downloadPDF()">📄 Download PDF</button>
    <div class="container">
        <div class="header">
            <h1>🏠 Real Estate Weekly</h1>
            <p>Your Premier Property Newsletter | Issue #47</p>
        </div>
        <div class="content">
            <h2>Featured Properties This Week</h2>
            
            <div class="property-card">
                <div class="property-image">🏡 Luxury Family Home</div>
                <div class="property-info">
                    <div class="property-price">$750,000</div>
                    <div class="property-details">4 Bed • 3 Bath • 2,500 sq ft • Downtown District</div>
                    <p>Beautiful modern home with updated kitchen, hardwood floors, and spacious backyard. Perfect for growing families.</p>
                    <a href="#" class="cta-button">View Details</a>
                </div>
            </div>
            
            <div class="property-card">
                <div class="property-image">🏢 Commercial Space</div>
                <div class="property-info">
                    <div class="property-price">$1,200,000</div>
                    <div class="property-details">Office Building • 5,000 sq ft • Business District</div>
                    <p>Prime commercial real estate opportunity in the heart of the business district. High foot traffic area.</p>
                    <a href="#" class="cta-button">Schedule Tour</a>
                </div>
            </div>
            
            <h3>Market Update</h3>
            <p>The real estate market continues to show strong growth with a 12% increase in property values this quarter. Interest rates remain favorable for qualified buyers.</p>
        </div>
        <div class="footer">
            <p>© 2024 Real Estate Weekly | Contact: info@realestateweekly.com</p>
        </div>
    </div>
    <script>
        function downloadPDF() {
            alert('PDF download feature would be implemented with server-side PDF generation');
        }
    </script>
</body>
</html>"""
    },
    "2": {
        "title": "Modern Business Landing Page",
        "category": "Landing Page",
        "downloadable": False,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CreditPro - Financial Solutions</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; }
        .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 100px 0; text-align: center; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .hero h1 { font-size: 48px; margin-bottom: 20px; font-weight: 700; }
        .hero p { font-size: 20px; margin-bottom: 30px; opacity: 0.9; }
        .cta-button { background: #ff6b6b; color: white; padding: 15px 30px; font-size: 18px; border: none; border-radius: 50px; cursor: pointer; transition: transform 0.3s; }
        .cta-button:hover { transform: translateY(-2px); }
        .features { padding: 80px 0; background: #f8f9fa; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; margin-top: 50px; }
        .feature-card { background: white; padding: 40px; border-radius: 10px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        .feature-icon { font-size: 48px; margin-bottom: 20px; }
        .feature-card h3 { font-size: 24px; margin-bottom: 15px; color: #333; }
        .stats { padding: 60px 0; background: #2c3e50; color: white; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center; }
        .stat-number { font-size: 48px; font-weight: bold; color: #3498db; }
        .testimonials { padding: 80px 0; }
        .testimonial { background: #f8f9fa; padding: 30px; border-radius: 10px; margin: 20px 0; }
        .footer { background: #2c3e50; color: white; padding: 40px 0; text-align: center; }
    </style>
</head>
<body>
    <section class="hero">
        <div class="container">
            <h1>Transform Your Credit Score</h1>
            <p>Professional credit repair and financial consulting services that deliver real results</p>
            <button class="cta-button">Get Started Today</button>
        </div>
    </section>
    
    <section class="features">
        <div class="container">
            <h2 style="text-align: center; font-size: 36px; margin-bottom: 20px;">Why Choose CreditPro?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📈</div>
                    <h3>Credit Score Improvement</h3>
                    <p>Average 100+ point increase in 6 months with our proven strategies and expert guidance.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🛡️</div>
                    <h3>Identity Protection</h3>
                    <p>Comprehensive monitoring and protection services to safeguard your financial identity.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💼</div>
                    <h3>Business Credit</h3>
                    <p>Build strong business credit profiles to access better financing and growth opportunities.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="stats">
        <div class="container">
            <div class="stats-grid">
                <div>
                    <div class="stat-number">50K+</div>
                    <p>Clients Served</p>
                </div>
                <div>
                    <div class="stat-number">98%</div>
                    <p>Success Rate</p>
                </div>
                <div>
                    <div class="stat-number">15+</div>
                    <p>Years Experience</p>
                </div>
                <div>
                    <div class="stat-number">24/7</div>
                    <p>Support Available</p>
                </div>
            </div>
        </div>
    </section>
    
    <section class="testimonials">
        <div class="container">
            <h2 style="text-align: center; font-size: 36px; margin-bottom: 40px;">What Our Clients Say</h2>
            <div class="testimonial">
                <p>"CreditPro helped me increase my credit score from 580 to 720 in just 8 months. Now I qualified for my dream home mortgage!"</p>
                <strong>- Sarah Johnson, Homeowner</strong>
            </div>
        </div>
    </section>
    
    <footer class="footer">
        <div class="container">
            <p>© 2024 CreditPro Financial Solutions. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    },
    "3": {
        "title": "Corporate Website - Real Estate Agency",
        "category": "Website",
        "downloadable": False,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premier Realty - Luxury Real Estate</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; }
        .navbar { background: rgba(255,255,255,0.95); padding: 15px 0; position: fixed; width: 100%; top: 0; z-index: 1000; backdrop-filter: blur(10px); }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }
        .logo { font-size: 24px; font-weight: bold; color: #2c3e50; }
        .nav-links { display: flex; list-style: none; gap: 30px; }
        .nav-links a { text-decoration: none; color: #333; font-weight: 500; transition: color 0.3s; }
        .nav-links a:hover { color: #3498db; }
        .hero { background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect fill="%23f0f0f0" width="1200" height="600"/><text x="600" y="300" text-anchor="middle" font-size="48" fill="%23666">Luxury Property Image</text></svg>'); background-size: cover; background-position: center; height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center; color: white; }
        .hero-content h1 { font-size: 56px; margin-bottom: 20px; font-weight: 300; }
        .hero-content p { font-size: 20px; margin-bottom: 30px; }
        .btn-primary { background: #3498db; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: 500; transition: background 0.3s; }
        .btn-primary:hover { background: #2980b9; }
        .section { padding: 80px 0; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .section-title { text-align: center; font-size: 36px; margin-bottom: 50px; color: #2c3e50; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
        .service-card { text-align: center; padding: 40px 20px; }
        .service-icon { font-size: 64px; margin-bottom: 20px; }
        .service-card h3 { font-size: 24px; margin-bottom: 15px; color: #2c3e50; }
        .about { background: #f8f9fa; }
        .about-content { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
        .about-text h2 { font-size: 36px; margin-bottom: 20px; color: #2c3e50; }
        .about-image { background: #ddd; height: 400px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; color: #666; }
        .contact { background: #2c3e50; color: white; }
        .contact-form { max-width: 600px; margin: 0 auto; }
        .form-group { margin-bottom: 20px; }
        .form-group input, .form-group textarea { width: 100%; padding: 15px; border: none; border-radius: 5px; font-size: 16px; }
        .btn-submit { background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .footer { background: #1a252f; color: white; padding: 40px 0; text-align: center; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">🏠 Premier Realty</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>
    
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>Luxury Real Estate Excellence</h1>
            <p>Discover premium properties with unmatched service and expertise</p>
            <a href="#contact" class="btn-primary">Find Your Dream Home</a>
        </div>
    </section>
    
    <section id="services" class="section">
        <div class="container">
            <h2 class="section-title">Our Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">🏡</div>
                    <h3>Residential Sales</h3>
                    <p>Expert guidance for buying and selling luxury residential properties with personalized service.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🏢</div>
                    <h3>Commercial Real Estate</h3>
                    <p>Strategic commercial property solutions for investors and businesses seeking prime locations.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">💼</div>
                    <h3>Investment Consulting</h3>
                    <p>Professional investment analysis and portfolio management for real estate investors.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section id="about" class="section about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>25 Years of Excellence</h2>
                    <p>Premier Realty has been the leading luxury real estate agency, serving discerning clients with exceptional properties and unmatched service. Our team of experienced professionals understands the unique needs of luxury property buyers and sellers.</p>
                    <p>With over $2 billion in sales and a reputation for excellence, we continue to set the standard for luxury real estate services.</p>
                </div>
                <div class="about-image">
                    Professional Team Photo
                </div>
            </div>
        </div>
    </section>
    
    <section id="contact" class="section contact">
        <div class="container">
            <h2 class="section-title">Contact Us</h2>
            <form class="contact-form">
                <div class="form-group">
                    <input type="text" placeholder="Your Name" required>
                </div>
                <div class="form-group">
                    <input type="email" placeholder="Your Email" required>
                </div>
                <div class="form-group">
                    <input type="tel" placeholder="Phone Number">
                </div>
                <div class="form-group">
                    <textarea rows="5" placeholder="How can we help you?" required></textarea>
                </div>
                <button type="submit" class="btn-submit">Send Message</button>
            </form>
        </div>
    </section>
    
    <footer class="footer">
        <div class="container">
            <p>© 2024 Premier Realty. All rights reserved. | Licensed Real Estate Broker</p>
        </div>
    </footer>
</body>
</html>"""
    },
    "4": {
        "title": "Streamlit Dashboard - Business Analytics",
        "category": "Streamlit",
        "downloadable": False,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Analytics Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f6; color: #333; }
        .streamlit-header { background: white; padding: 20px; border-bottom: 1px solid #e6e9ef; }
        .streamlit-header h1 { color: #ff4b4b; font-size: 28px; }
        .streamlit-sidebar { width: 300px; background: white; padding: 20px; position: fixed; height: 100vh; border-right: 1px solid #e6e9ef; }
        .streamlit-main { margin-left: 300px; padding: 20px; }
        .metric-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .metric-card { background: white; padding: 20px; border-radius: 10px; border: 1px solid #e6e9ef; }
        .metric-value { font-size: 32px; font-weight: bold; color: #ff4b4b; }
        .metric-label { color: #666; font-size: 14px; margin-top: 5px; }
        .metric-delta { font-size: 12px; margin-top: 5px; }
        .delta-positive { color: #00d4aa; }
        .delta-negative { color: #ff4b4b; }
        .chart-container { background: white; padding: 20px; border-radius: 10px; border: 1px solid #e6e9ef; margin-bottom: 20px; }
        .chart-placeholder { height: 300px; background: linear-gradient(45deg, #f0f2f6, #e6e9ef); display: flex; align-items: center; justify-content: center; border-radius: 5px; color: #666; font-size: 18px; }
        .sidebar-widget { margin-bottom: 20px; }
        .sidebar-widget label { display: block; margin-bottom: 5px; font-weight: 500; }
        .sidebar-widget select, .sidebar-widget input { width: 100%; padding: 8px; border: 1px solid #e6e9ef; border-radius: 5px; }
        .sidebar-widget button { width: 100%; padding: 10px; background: #ff4b4b; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .data-table { width: 100%; border-collapse: collapse; background: white; }
        .data-table th, .data-table td { padding: 12px; text-align: left; border-bottom: 1px solid #e6e9ef; }
        .data-table th { background: #f8f9fa; font-weight: 600; }
        .streamlit-expander { background: white; border: 1px solid #e6e9ef; border-radius: 10px; margin-bottom: 20px; }
        .expander-header { padding: 15px; cursor: pointer; font-weight: 500; }
        .expander-content { padding: 0 15px 15px; border-top: 1px solid #e6e9ef; }
    </style>
</head>
<body>
    <div class="streamlit-header">
        <h1>📊 Business Analytics Dashboard</h1>
        <p>Real-time insights and performance metrics for your business</p>
    </div>
    
    <div class="streamlit-sidebar">
        <h3>🎛️ Controls</h3>
        
        <div class="sidebar-widget">
            <label>Date Range</label>
            <select>
                <option>Last 7 days</option>
                <option>Last 30 days</option>
                <option>Last 90 days</option>
                <option>Last year</option>
            </select>
        </div>
        
        <div class="sidebar-widget">
            <label>Business Unit</label>
            <select>
                <option>All Units</option>
                <option>Sales</option>
                <option>Marketing</option>
                <option>Operations</option>
            </select>
        </div>
        
        <div class="sidebar-widget">
            <label>Metric Type</label>
            <select>
                <option>Revenue</option>
                <option>Customers</option>
                <option>Orders</option>
                <option>Conversion Rate</option>
            </select>
        </div>
        
        <div class="sidebar-widget">
            <button>🔄 Refresh Data</button>
        </div>
        
        <div class="sidebar-widget">
            <button>📥 Export Report</button>
        </div>
        
        <hr style="margin: 20px 0;">
        
        <div class="sidebar-widget">
            <h4>📈 Quick Stats</h4>
            <p><strong>Active Users:</strong> 1,247</p>
            <p><strong>Conversion Rate:</strong> 3.2%</p>
            <p><strong>Avg Order Value:</strong> $156</p>
        </div>
    </div>
    
    <div class="streamlit-main">
        <div class="metric-container">
            <div class="metric-card">
                <div class="metric-value">$127,450</div>
                <div class="metric-label">Total Revenue</div>
                <div class="metric-delta delta-positive">↗️ +12.5% from last month</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">2,847</div>
                <div class="metric-label">New Customers</div>
                <div class="metric-delta delta-positive">↗️ +8.3% from last month</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">1,923</div>
                <div class="metric-label">Orders</div>
                <div class="metric-delta delta-negative">↘️ -2.1% from last month</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">3.2%</div>
                <div class="metric-label">Conversion Rate</div>
                <div class="metric-delta delta-positive">↗️ +0.4% from last month</div>
            </div>
        </div>
        
        <div class="chart-container">
            <h3>📈 Revenue Trend</h3>
            <div class="chart-placeholder">
                Interactive Line Chart - Revenue Over Time
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div class="chart-container">
                <h3>🥧 Sales by Category</h3>
                <div class="chart-placeholder">
                    Pie Chart - Product Categories
                </div>
            </div>
            <div class="chart-container">
                <h3>📊 Monthly Comparison</h3>
                <div class="chart-placeholder">
                    Bar Chart - Month over Month
                </div>
            </div>
        </div>
        
        <div class="streamlit-expander">
            <div class="expander-header">📋 Recent Transactions</div>
            <div class="expander-content">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Customer</th>
                            <th>Amount</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>2024-01-15</td>
                            <td>John Smith</td>
                            <td>$245.00</td>
                            <td>✅ Completed</td>
                        </tr>
                        <tr>
                            <td>2024-01-15</td>
                            <td>Sarah Johnson</td>
                            <td>$189.50</td>
                            <td>⏳ Processing</td>
                        </tr>
                        <tr>
                            <td>2024-01-14</td>
                            <td>Mike Davis</td>
                            <td>$67.25</td>
                            <td>✅ Completed</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        
        <div class="streamlit-expander">
            <div class="expander-header">⚙️ Advanced Analytics</div>
            <div class="expander-content">
                <p>Configure advanced analytics settings and custom metrics here.</p>
                <div style="margin-top: 15px;">
                    <label>Custom Metric Formula:</label>
                    <input type="text" placeholder="(revenue - costs) / customers" style="width: 100%; margin-top: 5px;">
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
    },
    "5": {
        "title": "Business Letter - Credit Application Response",
        "category": "Business Letter",
        "downloadable": True,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Letter - Credit Application Response</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Times New Roman', serif; line-height: 1.6; color: #000; background: white; padding: 40px; }
        .letterhead { text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 20px; margin-bottom: 30px; }
        .company-name { font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 5px; }
        .company-info { font-size: 12px; color: #666; }
        .letter-container { max-width: 8.5in; margin: 0 auto; background: white; }
        .date { text-align: right; margin-bottom: 30px; font-size: 14px; }
        .recipient { margin-bottom: 30px; }
        .recipient-name { font-weight: bold; }
        .subject-line { font-weight: bold; margin-bottom: 20px; text-decoration: underline; }
        .salutation { margin-bottom: 20px; }
        .letter-body { margin-bottom: 30px; }
        .letter-body p { margin-bottom: 15px; text-align: justify; }
        .closing { margin-bottom: 60px; }
        .signature-block { margin-bottom: 20px; }
        .signature-line { border-bottom: 1px solid #000; width: 200px; margin-bottom: 5px; height: 40px; }
        .enclosures { margin-top: 20px; font-size: 12px; }
        .download-btn { position: fixed; top: 20px; right: 20px; background: #e74c3c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; }
        @media print {
            .download-btn { display: none; }
            body { padding: 0; }
        }
    </style>
</head>
<body>
    <button class="download-btn" onclick="downloadPDF()">📄 Download PDF</button>
    
    <div class="letter-container">
        <div class="letterhead">
            <div class="company-name">PREMIER FINANCIAL SERVICES</div>
            <div class="company-info">
                1234 Business Boulevard, Suite 500 | Financial District, NY 10001<br>
                Phone: (555) 123-4567 | Email: info@premierfinancial.com | www.premierfinancial.com
            </div>
        </div>
        
        <div class="date">
            January 15, 2024
        </div>
        
        <div class="recipient">
            <div class="recipient-name">Mr. Robert Anderson</div>
            <div>Chief Financial Officer</div>
            <div>Anderson Manufacturing Corp.</div>
            <div>5678 Industrial Way</div>
            <div>Manufacturing City, TX 75001</div>
        </div>
        
        <div class="subject-line">
            RE: Credit Application Approval - Account #CF-2024-0156
        </div>
        
        <div class="salutation">
            Dear Mr. Anderson:
        </div>
        
        <div class="letter-body">
            <p>We are pleased to inform you that your credit application submitted on December 28, 2023, has been approved. After careful review of your company's financial statements, credit history, and business references, we are confident in extending the following credit terms to Anderson Manufacturing Corp.</p>
            
            <p><strong>Approved Credit Limit:</strong> $500,000<br>
            <strong>Payment Terms:</strong> Net 30 days<br>
            <strong>Interest Rate:</strong> Prime + 2.5% (currently 8.0%)<br>
            <strong>Credit Line Type:</strong> Revolving Business Line of Credit</p>
            
            <p>This credit facility will provide your organization with the financial flexibility needed to support your expansion plans and manage seasonal cash flow variations. The credit line will be available for immediate use upon execution of the enclosed credit agreement.</p>
            
            <p>Please review the enclosed credit agreement carefully. Once signed and returned, along with the required insurance documentation, we will activate your account within 2-3 business days. Our relationship manager, Ms. Jennifer Walsh, will contact you this week to discuss the next steps and answer any questions you may have.</p>
            
            <p>We look forward to building a strong financial partnership with Anderson Manufacturing Corp. and supporting your continued growth and success.</p>
        </div>
        
        <div class="closing">
            <div>Sincerely,</div>
            <div class="signature-block">
                <div class="signature-line"></div>
                <div>Michael J. Thompson</div>
                <div>Senior Vice President, Commercial Lending</div>
                <div>Premier Financial Services</div>
            </div>
        </div>
        
        <div class="enclosures">
            <strong>Enclosures:</strong><br>
            • Credit Agreement (3 pages)<br>
            • Insurance Requirements Documentation<br>
            • Direct Deposit Authorization Form<br>
            • Welcome Package and Account Information
        </div>
        
        <div style="margin-top: 30px; font-size: 10px; color: #666; text-align: center;">
            This letter contains confidential and proprietary information. Distribution is restricted to authorized personnel only.
        </div>
    </div>
    
    <script>
        function downloadPDF() {
            alert('PDF download feature would be implemented with server-side PDF generation');
        }
    </script>
</body>
</html>"""
    },
    "6": {
        "title": "Email Sequence - Real Estate Lead Nurturing",
        "category": "Email Sequence",
        "downloadable": False,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Sequence - Real Estate Lead Nurturing</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; background: #f4f4f4; padding: 20px; }
        .sequence-container { max-width: 800px; margin: 0 auto; }
        .sequence-header { background: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }
        .email-card { background: white; margin-bottom: 20px; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .email-header { background: #3498db; color: white; padding: 15px; display: flex; justify-content: space-between; align-items: center; }
        .email-number { background: rgba(255,255,255,0.2); padding: 5px 10px; border-radius: 15px; font-size: 12px; }
        .email-content { padding: 25px; }
        .email-subject { font-size: 18px; font-weight: bold; margin-bottom: 15px; color: #2c3e50; }
        .email-body { line-height: 1.6; margin-bottom: 20px; }
        .email-body p { margin-bottom: 15px; }
        .cta-button { background: #e74c3c; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; display: inline-block; font-weight: bold; }
        .email-timing { background: #f8f9fa; padding: 10px 15px; border-left: 4px solid #3498db; margin-bottom: 15px; font-size: 14px; color: #666; }
        .sequence-stats { background: white; padding: 20px; border-radius: 0 0 10px 10px; display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; text-align: center; }
        .stat-item { }
        .stat-number { font-size: 24px; font-weight: bold; color: #3498db; }
        .stat-label { font-size: 12px; color: #666; }
        .personalization { background: #fff3cd; padding: 10px; border-radius: 5px; margin: 10px 0; font-size: 14px; }
    </style>
</head>
<body>
    <div class="sequence-container">
        <div class="sequence-header">
            <h1>🏠 Real Estate Lead Nurturing Sequence</h1>
            <p>7-Email Automated Series for Converting Property Inquiries</p>
        </div>
        
        <div class="sequence-stats">
            <div class="stat-item">
                <div class="stat-number">7</div>
                <div class="stat-label">Total Emails</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">21</div>
                <div class="stat-label">Days Duration</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">34%</div>
                <div class="stat-label">Avg Open Rate</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">12%</div>
                <div class="stat-label">Conversion Rate</div>
            </div>
        </div>
        
         Email 1 
        <div class="email-card">
            <div class="email-header">
                <h3>Welcome Email</h3>
                <div class="email-number">Email 1</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent immediately after lead capture</div>
                <div class="email-subject">Welcome! Your Dream Home Journey Starts Here 🏡</div>
                <div class="personalization">💡 Personalization: {First_Name}, {Property_Interest}, {Location_Preference}</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>Thank you for your interest in {Property_Interest} in {Location_Preference}! I'm Sarah Martinez, your dedicated real estate advisor, and I'm excited to help you find the perfect property.</p>
                    <p>Over the next few weeks, I'll be sharing valuable insights about the local market, exclusive property listings, and expert tips to make your home buying journey smooth and successful.</p>
                    <p>To get started, I've prepared a personalized market report for {Location_Preference} that shows current trends, pricing, and available properties that match your criteria.</p>
                </div>
                <a href="#" class="cta-button">Get Your Free Market Report</a>
            </div>
        </div>
        
         Email 2 
        <div class="email-card">
            <div class="email-header">
                <h3>Market Insights</h3>
                <div class="email-number">Email 2</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 2 days after Email 1</div>
                <div class="email-subject">Market Update: What's Happening in {Location_Preference} 📈</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>The {Location_Preference} market is showing some interesting trends this month. Here are the key insights you should know:</p>
                    <p>• Average home prices have increased 8% compared to last year<br>
                    • Inventory is up 15%, giving buyers more options<br>
                    • Properties are selling within 18 days on average<br>
                    • Interest rates remain favorable for qualified buyers</p>
                    <p>This means it's still a great time to buy, especially with the increased inventory giving you more negotiating power.</p>
                </div>
                <a href="#" class="cta-button">View Current Listings</a>
            </div>
        </div>
        
         Email 3 
        <div class="email-card">
            <div class="email-header">
                <h3>Exclusive Listings</h3>
                <div class="email-number">Email 3</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 5 days after Email 2</div>
                <div class="email-subject">🔥 Hot Properties Just Listed in {Location_Preference}</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>I wanted to give you first access to these amazing properties that just hit the market:</p>
                    <p><strong>1. Modern Family Home - $485,000</strong><br>
                    4 bed, 3 bath • 2,200 sq ft • Updated kitchen • Large backyard</p>
                    <p><strong>2. Luxury Condo - $320,000</strong><br>
                    2 bed, 2 bath • Downtown location • Amenities included • City views</p>
                    <p>These properties match your criteria for {Property_Interest} and are priced competitively for the current market.</p>
                </div>
                <a href="#" class="cta-button">Schedule Private Showing</a>
            </div>
        </div>
        
         Email 4 
        <div class="email-card">
            <div class="email-header">
                <h3>Buyer's Guide</h3>
                <div class="email-number">Email 4</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 3 days after Email 3</div>
                <div class="email-subject">Your Complete Home Buying Checklist 📋</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>Buying a home can feel overwhelming, but with the right preparation, it becomes much easier. Here's your step-by-step checklist:</p>
                    <p><strong>Before You Start:</strong><br>
                    ✓ Get pre-approved for a mortgage<br>
                    ✓ Determine your budget and must-haves<br>
                    ✓ Research neighborhoods and schools</p>
                    <p><strong>During Your Search:</strong><br>
                    ✓ Work with a trusted real estate agent<br>
                    ✓ Schedule home inspections<br>
                    ✓ Review comparable sales</p>
                    <p>I've created a detailed guide that covers each step in detail, plus local resources specific to {Location_Preference}.</p>
                </div>
                <a href="#" class="cta-button">Download Complete Guide</a>
            </div>
        </div>
        
         Email 5 
        <div class="email-card">
            <div class="email-header">
                <h3>Success Stories</h3>
                <div class="email-number">Email 5</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 4 days after Email 4</div>
                <div class="email-subject">How I Helped the Johnson Family Find Their Dream Home 🏠</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>I wanted to share a recent success story that might inspire you. The Johnson family came to me looking for a {Property_Interest} in {Location_Preference}, just like you.</p>
                    <p>They had been searching for 6 months with another agent but weren't finding the right fit. Within 3 weeks of working together, we found their perfect home - and negotiated $15,000 below asking price!</p>
                    <p>"Sarah understood exactly what we were looking for and made the entire process stress-free. We couldn't be happier with our new home!" - Mike & Lisa Johnson</p>
                    <p>Every client's situation is unique, but with the right strategy and market knowledge, we can find your perfect property too.</p>
                </div>
                <a href="#" class="cta-button">Read More Success Stories</a>
            </div>
        </div>
        
         Email 6 
        <div class="email-card">
            <div class="email-header">
                <h3>Financing Options</h3>
                <div class="email-number">Email 6</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 3 days after Email 5</div>
                <div class="email-subject">Financing Made Simple: Your Mortgage Options Explained 💰</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>One of the most common questions I get is about financing options. Let me break down the main types of mortgages available:</p>
                    <p><strong>Conventional Loans:</strong> Great for buyers with good credit and 10-20% down payment<br>
                    <strong>FHA Loans:</strong> Perfect for first-time buyers with as little as 3.5% down<br>
                    <strong>VA Loans:</strong> Excellent benefits for military veterans<br>
                    <strong>USDA Loans:</strong> Zero down payment options for rural properties</p>
                    <p>I work with several trusted lenders who can help you find the best rates and terms for your situation. Getting pre-approved is the first step to making competitive offers.</p>
                </div>
                <a href="#" class="cta-button">Connect with Preferred Lenders</a>
            </div>
        </div>
        
         Email 7 
        <div class="email-card">
            <div class="email-header">
                <h3>Call to Action</h3>
                <div class="email-number">Email 7</div>
            </div>
            <div class="email-content">
                <div class="email-timing">⏰ Sent 4 days after Email 6</div>
                <div class="email-subject">Ready to Find Your Dream Home? Let's Talk! 📞</div>
                <div class="email-body">
                    <p>Hi {First_Name},</p>
                    <p>Over the past few weeks, I've shared market insights, exclusive listings, and valuable resources to help with your home search in {Location_Preference}.</p>
                    <p>Now I'd love to have a personal conversation about your specific needs and how I can help you find the perfect {Property_Interest}.</p>
                    <p>During our 15-minute consultation, we'll discuss:</p>
                    <p>• Your specific requirements and timeline<br>
                    • Current market opportunities<br>
                    • My proven process for finding and securing your ideal property<br>
                    • Next steps to get started</p>
                    <p>I have limited availability this week, so let's schedule a time that works for you.</p>
                </div>
                <a href="#" class="cta-button">Schedule Your Free Consultation</a>
            </div>
        </div>
    </div>
</body>
</html>"""
    },
    "7": {
        "title": "Professional Invoice - Business Services",
        "category": "Invoice",
        "downloadable": True,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Invoice #INV-2024-0156</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; line-height: 1.4; color: #333; background: white; }
        .invoice-container { max-width: 8.5in; margin: 0 auto; padding: 40px; background: white; }
        .invoice-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 40px; }
        .company-info h1 { color: #2c3e50; font-size: 28px; margin-bottom: 10px; }
        .company-info p { color: #666; font-size: 14px; line-height: 1.4; }
        .invoice-title { text-align: right; }
        .invoice-title h2 { font-size: 36px; color: #e74c3c; margin-bottom: 10px; }
        .invoice-number { font-size: 18px; color: #666; }
        .invoice-details { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 40px; }
        .bill-to, .invoice-info { }
        .bill-to h3, .invoice-info h3 { color: #2c3e50; margin-bottom: 15px; font-size: 16px; }
        .bill-to p, .invoice-info p { margin-bottom: 5px; }
        .invoice-table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
        .invoice-table th { background: #2c3e50; color: white; padding: 15px; text-align: left; font-weight: 600; }
        .invoice-table td { padding: 15px; border-bottom: 1px solid #eee; }
        .invoice-table tr:nth-child(even) { background: #f9f9f9; }
        .quantity, .rate, .amount { text-align: right; }
        .invoice-totals { margin-left: auto; width: 300px; }
        .total-row { display: flex; justify-content: space-between; padding: 8px 0; }
        .total-row.subtotal { border-bottom: 1px solid #eee; }
        .total-row.final { border-top: 2px solid #2c3e50; font-weight: bold; font-size: 18px; color: #2c3e50; }
        .invoice-notes { margin-top: 40px; }
        .invoice-notes h3 { color: #2c3e50; margin-bottom: 15px; }
        .invoice-notes p { color: #666; line-height: 1.6; }
        .payment-terms { background: #f8f9fa; padding: 20px; border-left: 4px solid #3498db; margin-top: 30px; }
        .payment-terms h3 { color: #2c3e50; margin-bottom: 10px; }
        .footer { margin-top: 40px; text-align: center; color: #666; font-size: 12px; border-top: 1px solid #eee; padding-top: 20px; }
        .download-btn { position: fixed; top: 20px; right: 20px; background: #e74c3c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; }
        @media print {
            .download-btn { display: none; }
            body { padding: 0; }
        }
    </style>
</head>
<body>
    <button class="download-btn" onclick="downloadPDF()">📄 Download PDF</button>
    
    <div class="invoice-container">
        <div class="invoice-header">
            <div class="company-info">
                <h1>PREMIER BUSINESS SOLUTIONS</h1>
                <p>
                    1234 Corporate Drive, Suite 200<br>
                    Business City, NY 10001<br>
                    Phone: (555) 123-4567<br>
                    Email: billing@premierbusiness.com<br>
                    Tax ID: 12-3456789
                </p>
            </div>
            <div class="invoice-title">
                <h2>INVOICE</h2>
                <div class="invoice-number">#INV-2024-0156</div>
            </div>
        </div>
        
        <div class="invoice-details">
            <div class="bill-to">
                <h3>BILL TO:</h3>
                <p><strong>Anderson Manufacturing Corp.</strong></p>
                <p>Robert Anderson, CFO</p>
                <p>5678 Industrial Way</p>
                <p>Manufacturing City, TX 75001</p>
                <p>Phone: (555) 987-6543</p>
                <p>Email: r.anderson@andersonmfg.com</p>
            </div>
            <div class="invoice-info">
                <h3>INVOICE DETAILS:</h3>
                <p><strong>Invoice Date:</strong> January 15, 2024</p>
                <p><strong>Due Date:</strong> February 14, 2024</p>
                <p><strong>Payment Terms:</strong> Net 30</p>
                <p><strong>Project:</strong> Q4 Financial Consulting</p>
                <p><strong>PO Number:</strong> PO-2024-0089</p>
            </div>
        </div>
        
        <table class="invoice-table">
            <thead>
                <tr>
                    <th>Description</th>
                    <th class="quantity">Qty</th>
                    <th class="rate">Rate</th>
                    <th class="amount">Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <strong>Financial Analysis & Reporting</strong><br>
                        Comprehensive financial analysis including cash flow projections, budget variance analysis, and quarterly financial reporting for Q4 2023.
                    </td>
                    <td class="quantity">40 hrs</td>
                    <td class="rate">$150.00</td>
                    <td class="amount">$6,000.00</td>
                </tr>
                <tr>
                    <td>
                        <strong>Strategic Planning Consultation</strong><br>
                        Executive-level strategic planning sessions including market analysis, competitive positioning, and 2024 growth strategy development.
                    </td>
                    <td class="quantity">24 hrs</td>
                    <td class="rate">$200.00</td>
                    <td class="amount">$4,800.00</td>
                </tr>
                <tr>
                    <td>
                        <strong>Process Optimization Review</strong><br>
                        Operational efficiency assessment and process improvement recommendations for manufacturing and supply chain operations.
                    </td>
                    <td class="quantity">32 hrs</td>
                    <td class="rate">$175.00</td>
                    <td class="amount">$5,600.00</td>
                </tr>
                <tr>
                    <td>
                        <strong>Compliance Audit Support</strong><br>
                        Assistance with regulatory compliance review and documentation preparation for annual audit requirements.
                    </td>
                    <td class="quantity">16 hrs</td>
                    <td class="rate">$125.00</td>
                    <td class="amount">$2,000.00</td>
                </tr>
                <tr>
                    <td>
                        <strong>Executive Presentation Materials</strong><br>
                        Creation of board presentation materials including financial dashboards, executive summaries, and strategic recommendations.
                    </td>
                    <td class="quantity">1</td>
                    <td class="rate">$1,500.00</td>
                    <td class="amount">$1,500.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="invoice-totals">
            <div class="total-row subtotal">
                <span>Subtotal:</span>
                <span>$19,900.00</span>
            </div>
            <div class="total-row">
                <span>Tax (8.25%):</span>
                <span>$1,641.75</span>
            </div>
            <div class="total-row final">
                <span>Total Amount Due:</span>
                <span>$21,541.75</span>
            </div>
        </div>
        
        <div class="payment-terms">
            <h3>Payment Information</h3>
            <p><strong>Payment Methods:</strong> Check, ACH Transfer, Wire Transfer</p>
            <p><strong>Bank Details:</strong> First National Bank | Routing: 123456789 | Account: 987654321</p>
            <p><strong>Remit to:</strong> Premier Business Solutions, 1234 Corporate Drive, Suite 200, Business City, NY 10001</p>
        </div>
        
        <div class="invoice-notes">
            <h3>Terms & Conditions</h3>
            <p>Payment is due within 30 days of invoice date. A 1.5% monthly service charge will be applied to past due accounts. All work performed is subject to our standard terms and conditions. Thank you for your business!</p>
        </div>
        
        <div class="footer">
            <p>This invoice was generated electronically and is valid without signature.</p>
            <p>For questions regarding this invoice, please contact our billing department at billing@premierbusiness.com</p>
        </div>
    </div>
    
    <script>
        function downloadPDF() {
            alert('PDF download feature would be implemented with server-side PDF generation');
        }
    </script>
</body>
</html>"""
    },
    "8": {
        "title": "Business Contract - Real Estate Purchase Agreement",
        "category": "Business Contract",
        "downloadable": True,
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Purchase Agreement</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Times New Roman', serif; line-height: 1.5; color: #000; background: white; padding: 30px; }
        .contract-container { max-width: 8.5in; margin: 0 auto; background: white; }
        .contract-header { text-align: center; margin-bottom: 30px; border-bottom: 2px solid #000; padding-bottom: 20px; }
        .contract-title { font-size: 20px; font-weight: bold; margin-bottom: 10px; }
        .contract-subtitle { font-size: 14px; }
        .section { margin-bottom: 25px; }
        .section-title { font-weight: bold; font-size: 14px; margin-bottom: 10px; text-decoration: underline; }
        .section-content { text-align: justify; }
        .section-content p { margin-bottom: 10px; }
        .parties-info { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 25px; }
        .party-box { border: 1px solid #000; padding: 15px; }
        .party-title { font-weight: bold; text-align: center; margin-bottom: 10px; }
        .property-details { border: 1px solid #000; padding: 15px; margin: 15px 0; }
        .terms-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 15px 0; }
        .signature-section { margin-top: 40px; }
        .signature-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px; }
        .signature-block { }
        .signature-line { border-bottom: 1px solid #000; height: 40px; margin-bottom: 5px; }
        .signature-label { font-size: 12px; text-align: center; }
        .date-line { border-bottom: 1px solid #000; width: 150px; display: inline-block; margin-left: 10px; }
        .checkbox { display: inline-block; width: 15px; height: 15px; border: 1px solid #000; margin-right: 5px; vertical-align: middle; }
        .download-btn { position: fixed; top: 20px; right: 20px; background: #e74c3c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; }
        @media print {
            .download-btn { display: none; }
            body { padding: 0; }
        }
    </style>
</head>
<body>
    <button class="download-btn" onclick="downloadPDF()">📄 Download PDF</button>
    
    <div class="contract-container">
        <div class="contract-header">
            <div class="contract-title">REAL ESTATE PURCHASE AGREEMENT</div>
            <div class="contract-subtitle">State of Texas | Contract No. REA-2024-0156</div>
        </div>
        
        <div class="parties-info">
            <div class="party-box">
                <div class="party-title">BUYER</div>
                <p><strong>Name:</strong> Michael and Jennifer Thompson</p>
                <p><strong>Address:</strong> 789 Buyer Lane<br>Current City, TX 75002</p>
                <p><strong>Phone:</strong> (555) 234-5678</p>
                <p><strong>Email:</strong> mthompson@email.com</p>
            </div>
            <div class="party-box">
                <div class="party-title">SELLER</div>
                <p><strong>Name:</strong> Robert and Susan Martinez</p>
                <p><strong>Address:</strong> 1456 Seller Street<br>Property City, TX 75003</p>
                <p><strong>Phone:</strong> (555) 345-6789</p>
                <p><strong>Email:</strong> rmartinez@email.com</p>
            </div>
        </div>
        
        <div class="property-details">
            <div class="section-title">PROPERTY DESCRIPTION</div>
            <p><strong>Address:</strong> 1456 Seller Street, Property City, TX 75003</p>
            <p><strong>Legal Description:</strong> Lot 15, Block 8, Meadowbrook Subdivision, Property City, Dallas County, Texas</p>
            <p><strong>Property Type:</strong> Single Family Residence</p>
            <p><strong>Square Footage:</strong> 2,450 sq ft (approximate)</p>
            <p><strong>Lot Size:</strong> 0.25 acres</p>
            <p><strong>Year Built:</strong> 2018</p>
        </div>
        
        <div class="section">
            <div class="section-title">1. PURCHASE PRICE AND TERMS</div>
            <div class="section-content">
                <div class="terms-grid">
                    <div>
                        <p><strong>Purchase Price:</strong> $485,000.00</p>
                        <p><strong>Earnest Money:</strong> $10,000.00</p>
                        <p><strong>Down Payment:</strong> $97,000.00 (20%)</p>
                    </div>
                    <div>
                        <p><strong>Loan Amount:</strong> $388,000.00</p>
                        <p><strong>Closing Costs:</strong> As per lender requirements</p>
                        <p><strong>Financing Type:</strong> Conventional Mortgage</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">2. CLOSING AND POSSESSION</div>
            <div class="section-content">
                <p><strong>Closing Date:</strong> March 15, 2024, or such earlier date as mutually agreed upon by both parties.</p>
                <p><strong>Possession:</strong> Buyer shall receive possession of the property at closing, subject to existing leases if any.</p>
                <p><strong>Closing Location:</strong> Title company office to be mutually agreed upon by both parties.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">3. FINANCING CONTINGENCY</div>
            <div class="section-content">
                <p>This offer is contingent upon Buyer obtaining a firm commitment for financing within 21 days from the effective date of this contract. Buyer agrees to make application for financing within 5 days of the effective date and to provide all required documentation to the lender in a timely manner.</p>
                <p><strong>Loan Terms:</strong> Interest rate not to exceed 7.5% per annum, 30-year fixed rate mortgage.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">4. INSPECTION CONTINGENCY</div>
            <div class="section-content">
                <p>Buyer shall have 10 days from the effective date to conduct inspections of the property, including but not limited to:</p>
                <p><span class="checkbox"></span> General home inspection<br>
                <span class="checkbox"></span> Termite/pest inspection<br>
                <span class="checkbox"></span> HVAC system inspection<br>
                <span class="checkbox"></span> Roof inspection<br>
                <span class="checkbox"></span> Plumbing and electrical inspection</p>
                <p>All inspections shall be at Buyer's expense. Buyer may request repairs or credits based on inspection results.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">5. TITLE AND SURVEY</div>
            <div class="section-content">
                <p>Seller shall provide a current title commitment and survey at Seller's expense. Title shall be marketable and insurable. Any title defects must be cured prior to closing or this contract may be terminated at Buyer's option.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">6. PROPERTY CONDITION</div>
            <div class="section-content">
                <p>Property is sold in "as-is" condition, subject to inspection contingencies. Seller warrants that all systems (HVAC, plumbing, electrical) will be in working order at closing. Property includes all fixtures, built-in appliances, and items specifically listed in attached addendum.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">7. DEFAULT AND REMEDIES</div>
            <div class="section-content">
                <p>If Buyer defaults, Seller may retain earnest money as liquidated damages. If Seller defaults, Buyer may seek specific performance or damages. Time is of the essence in this contract.</p>
            </div>
        </div>
        
        <div class="section">
            <div class="section-title">8. ADDITIONAL TERMS</div>
            <div class="section-content">
                <p>• Property taxes and HOA fees shall be prorated as of closing date<br>
                • Seller to provide home warranty policy at closing<br>
                • All negotiations and modifications must be in writing<br>
                • This contract shall be binding upon heirs and assigns<br>
                • Governing law: State of Texas</p>
            </div>
        </div>
        
        <div class="signature-section">
            <div class="section-title">SIGNATURES</div>
            <p>By signing below, the parties agree to the terms and conditions set forth in this Real Estate Purchase Agreement.</p>
            
            <div class="signature-grid">
                <div class="signature-block">
                    <p><strong>BUYER:</strong></p>
                    <div class="signature-line"></div>
                    <div class="signature-label">Michael Thompson</div>
                    <p>Date: <span class="date-line"></span></p>
                    <br>
                    <div class="signature-line"></div>
                    <div class="signature-label">Jennifer Thompson</div>
                    <p>Date: <span class="date-line"></span></p>
                </div>
                <div class="signature-block">
                    <p><strong>SELLER:</strong></p>
                    <div class="signature-line"></div>
                    <div class="signature-label">Robert Martinez</div>
                    <p>Date: <span class="date-line"></span></p>
                    <br>
                    <div class="signature-line"></div>
                    <div class="signature-label">Susan Martinez</div>
                    <p>Date: <span class="date-line"></span></p>
                </div>
            </div>
            
            <div style="margin-top: 30px; text-align: center; font-size: 12px;">
                <p><strong>REAL ESTATE AGENTS:</strong></p>
                <p>Buyer's Agent: Sarah Johnson, Premier Realty | License #123456</p>
                <p>Seller's Agent: David Wilson, Elite Properties | License #789012</p>
            </div>
        </div>
        
        <div style="margin-top: 30px; font-size: 10px; text-align: center; border-top: 1px solid #000; padding-top: 15px;">
            <p>This contract has been prepared by real estate professionals and reviewed by legal counsel. All parties are advised to seek independent legal advice before signing.</p>
        </div>
    </div>
    
    <script>
        function downloadPDF() {
            alert('PDF download feature would be implemented with server-side PDF generation');
        }
    </script>
</body>
</html>"""
    }
}

# --- LOAD DATA FUNCTION ---
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        # Check for required columns - now supporting full demo structure
        required_columns = ['Number', 'Code']
        optional_columns = ['Title', 'Category', 'Description', 'PDF_Enabled']
        
        # Ensure required columns exist
        for col in required_columns:
            if col not in df.columns:
                st.error(f"Google Sheet must have '{col}' column.")
                return pd.DataFrame(columns=required_columns + optional_columns)
        
        # Add missing optional columns with defaults
        for col in optional_columns:
            if col not in df.columns:
                if col == 'Title':
                    df[col] = df['Number'].astype(str) + " - Custom Code"
                elif col == 'Category':
                    df[col] = "Custom"
                elif col == 'Description':
                    df[col] = "Custom HTML/CSS code from Google Sheets"
                elif col == 'PDF_Enabled':
                    df[col] = False
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame(columns=['Number', 'Code', 'Title', 'Category', 'Description', 'PDF_Enabled'])

def generate_pdf_from_html(html_content, title="Document"):
    """Generate PDF from HTML content using reportlab with better HTML parsing"""
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib.colors import HexColor
        from io import BytesIO
        import re
        from html.parser import HTMLParser
        
        class HTMLToPDFParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.content = []
                self.current_text = ""
                self.in_style = False
                self.in_script = False
                self.in_title = False
                self.in_header = False
                self.header_level = 0
                
            def handle_starttag(self, tag, attrs):
                if tag == 'style' or tag == 'script':
                    self.in_style = True
                    self.in_script = True
                elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    self.in_header = True
                    self.header_level = int(tag[1])
                elif tag == 'title':
                    self.in_title = True
                elif tag in ['p', 'div', 'br']:
                    if self.current_text.strip():
                        self.content.append(('text', self.current_text.strip()))
                        self.current_text = ""
                    if tag == 'br':
                        self.content.append(('break', ''))
                        
            def handle_endtag(self, tag):
                if tag == 'style' or tag == 'script':
                    self.in_style = False
                    self.in_script = False
                elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    if self.current_text.strip():
                        self.content.append(('header', self.current_text.strip(), self.header_level))
                        self.current_text = ""
                    self.in_header = False
                    self.header_level = 0
                elif tag == 'title':
                    self.in_title = False
                elif tag in ['p', 'div']:
                    if self.current_text.strip():
                        self.content.append(('text', self.current_text.strip()))
                        self.current_text = ""
                        
            def handle_data(self, data):
                if not self.in_style and not self.in_script and not self.in_title:
                    self.current_text += data
                    
            def get_content(self):
                if self.current_text.strip():
                    self.content.append(('text', self.current_text.strip()))
                return self.content
        
        # Create a BytesIO buffer
        buffer = BytesIO()
        
        # Create PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=1*inch)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            textColor=HexColor('#2c3e50'),
            alignment=1  # Center alignment
        )
        
        header_styles = {
            1: ParagraphStyle('Header1', parent=styles['Heading1'], fontSize=16, spaceAfter=20, textColor=HexColor('#34495e')),
            2: ParagraphStyle('Header2', parent=styles['Heading2'], fontSize=14, spaceAfter=15, textColor=HexColor('#34495e')),
            3: ParagraphStyle('Header3', parent=styles['Heading3'], fontSize=12, spaceAfter=12, textColor=HexColor('#34495e')),
        }
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=12,
            textColor=HexColor('#2c3e50'),
            leading=14
        )
        
        # Add title
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 20))
        
        # Parse HTML content
        parser = HTMLToPDFParser()
        parser.feed(html_content)
        content_items = parser.get_content()
        
        # Convert parsed content to PDF elements
        for item in content_items:
            if item[0] == 'header':
                level = min(item[2], 3)  # Cap at h3
                style = header_styles.get(level, header_styles[3])
                story.append(Paragraph(item[1], style))
            elif item[0] == 'text':
                # Clean up text and add as paragraph
                clean_text = item[1].replace('&nbsp;', ' ').replace('&amp;', '&')
                if clean_text.strip():
                    story.append(Paragraph(clean_text, body_style))
            elif item[0] == 'break':
                story.append(Spacer(1, 6))
        
        # If no content was parsed, fall back to simple text extraction
        if not content_items:
            clean_text = re.sub('<[^<]+?>', '', html_content)
            clean_text = clean_text.replace('&nbsp;', ' ').replace('&amp;', '&')
            paragraphs = [p.strip() for p in clean_text.split('\n') if p.strip()]
            
            for para in paragraphs:
                story.append(Paragraph(para, body_style))
                story.append(Spacer(1, 8))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
        
    except ImportError:
        return None
    except Exception as e:
        print(f"PDF generation error: {e}")
        return None

def clean_html_for_download(html_content):
    """Clean and structure HTML for download"""
    # Ensure proper HTML structure
    if not html_content.strip().startswith('<!DOCTYPE html>'):
        if '<html>' not in html_content:
            # Wrap in basic HTML structure if missing
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Downloaded Content</title>
</head>
<body>
{html_content}
</body>
</html>"""
    return html_content

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Enhanced Code Viewer with Demo Examples",
    layout="wide"
)

# --- TITLE ---
st.title("🚀 Enhanced Code Viewer with Demo Examples")
st.markdown(
    """
    Professional code viewer with 8 comprehensive demo examples and enhanced editing capabilities.
    Choose from demo examples or load from Google Sheets.
    """
)

# --- SIDEBAR ---
st.sidebar.title("🎯 Code Selection")

# Data source selection
data_source = st.sidebar.radio(
    "Choose Data Source:",
    ["📋 Demo Examples", "📊 Google Sheets"],
    index=0  # Default to demo examples
)

if data_source == "📋 Demo Examples":
    # Demo examples selection
    st.sidebar.markdown("### Available Demo Examples")
    
    # Category filter
    categories = list(set([example["category"] for example in DEMO_EXAMPLES.values()]))
    selected_category = st.sidebar.selectbox("Filter by Category:", ["All Categories"] + categories)
    
    # Filter examples by category
    if selected_category == "All Categories":
        filtered_examples = DEMO_EXAMPLES
    else:
        filtered_examples = {k: v for k, v in DEMO_EXAMPLES.items() if v["category"] == selected_category}
    
    # Example selection
    example_options = [f"{k}. {v['title']} ({v['category']})" for k, v in filtered_examples.items()]
    selected_example = st.sidebar.selectbox("Choose Example:", example_options)
    
    # Extract number from selection
    selected_number = selected_example.split(".")[0]
    current_code = DEMO_EXAMPLES[selected_number]["code"]
    example_info = DEMO_EXAMPLES[selected_number]
    
else:
    sheet_url = st.sidebar.text_input(
        "Google Sheet CSV URL:",
        value="https://docs.google.com/spreadsheets/d/1eFZcnDoGT2NJHaEQSgxW5psN5kvlkYx1vtuXGRFTGTk/export?format=csv",
        help="Enter the CSV export URL of your Google Sheet. Required columns: Number, Code. Optional: Title, Category, Description, PDF_Enabled"
    )
    
    if sheet_url:
        df = load_data(sheet_url)
        
        if not df.empty:
            st.sidebar.markdown("### Google Sheets Data")
            
            # Category filter for Google Sheets
            if 'Category' in df.columns:
                sheet_categories = list(set(df['Category'].tolist()))
                selected_sheet_category = st.sidebar.selectbox("Filter by Category:", ["All Categories"] + sheet_categories)
                
                if selected_sheet_category != "All Categories":
                    df = df[df['Category'] == selected_sheet_category]
            
            # Search functionality
            search_number = st.sidebar.text_input("🔍 Search Number", placeholder="Type to filter...")
            numbers = df['Number'].astype(str).tolist()
            
            # Filter numbers by search term
            if search_number:
                filtered_numbers = [n for n in numbers if search_number.lower() in n.lower()]
                if not filtered_numbers:
                    st.sidebar.warning("No matching numbers found")
                    filtered_numbers = numbers
            else:
                filtered_numbers = numbers
            
            if 'Title' in df.columns and 'Category' in df.columns:
                selection_options = []
                for num in filtered_numbers:
                    row = df[df['Number'].astype(str) == num].iloc[0]
                    title = row.get('Title', f"Item {num}")
                    category = row.get('Category', 'Custom')
                    selection_options.append(f"{num}. {title} ({category})")
                
                selected_display = st.sidebar.selectbox("Choose Item:", selection_options)
                selected_number = selected_display.split(".")[0]
            else:
                selected_number = st.sidebar.selectbox("Choose Number", filtered_numbers)
            
            # Get code and info from sheet
            selected_row = df[df['Number'].astype(str) == selected_number]
            if not selected_row.empty:
                row_data = selected_row.iloc[0]
                current_code = row_data['Code']
                
                example_info = {
                    'title': row_data.get('Title', f"Item {selected_number}"),
                    'category': row_data.get('Category', 'Custom'),
                    'description': row_data.get('Description', 'Custom HTML/CSS code from Google Sheets'),
                    'pdf_enabled': row_data.get('PDF_Enabled', False)
                }
            else:
                current_code = "<p>No code available for this number</p>"
                example_info = None
        else:
            st.sidebar.error("Unable to load data from Google Sheets")
            current_code = "<p>No data available</p>"
            example_info = None
    else:
        current_code = "<p>Please enter a Google Sheet URL</p>"
        example_info = None

# --- CONTROL TOGGLES ---
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Display Controls")

live_preview = st.sidebar.toggle("🌐 Live Preview", value=True, help="Enable/disable live preview")
show_code = st.sidebar.toggle("👁️ Show Code Panel", value=False, help="Toggle code visibility")  # Default to False

halt_edit = st.sidebar.toggle("🔒 Lock Edit Mode", value=False, help="Lock editing to prevent accidental changes")
edit_mode = st.sidebar.toggle("✏️ Edit Mode", value=False, help="Enable to edit the code", disabled=halt_edit)

if halt_edit and edit_mode:
    st.sidebar.warning("🔒 Edit mode is locked. Disable lock to edit.")

# --- EDIT MODE HANDLING ---
if edit_mode and show_code:
    if 'edited_code' not in st.session_state:
        st.session_state.edited_code = current_code
    
    # Reset button
    if st.sidebar.button("🔄 Reset to Original", help="Reset edited code to original"):
        st.session_state.edited_code = current_code
        st.rerun()

# Determine which code to use
if edit_mode and 'edited_code' in st.session_state:
    display_code = st.session_state.edited_code
else:
    display_code = current_code

# --- MAIN LAYOUT ---
if live_preview and show_code:
    col1, col2 = st.columns([1, 1])
elif live_preview:
    col1 = st.container()
    col2 = None
elif show_code:
    col1 = None
    col2 = st.container()
else:
    st.info("Both preview and code panel are disabled. Please enable at least one from the sidebar.")
    st.stop()

# --- LIVE PREVIEW ---
if live_preview:
    with col1 if col2 else st.container():
        if data_source == "📋 Demo Examples" and example_info:
            st.subheader(f"🌐 {example_info['title']}")
            st.caption(f"Category: {example_info['category']} | {'📄 PDF Downloadable' if example_info['downloadable'] else '🌐 Web Only'}")
        else:
            st.subheader(f"🌐 Live Preview - Number: {selected_number}")
        
        if edit_mode:
            st.caption("⚡ Live editing mode - changes update in real-time")
        
        try:
            st.components.v1.html(display_code, height=700, scrolling=True)
        except Exception as e:
            st.error(f"Error rendering preview: {str(e)}")

# --- CODE EDITOR/VIEWER ---
if show_code:
    with col2 if col1 else st.container():
        if edit_mode:
            st.subheader("✏️ Enhanced Code Editor")
            st.caption("Edit the code below - changes apply to preview immediately")
            
            edited_code = st.text_area(
                "HTML/CSS Code",
                value=display_code,
                height=600,  # Increased height
                key="code_editor",
                label_visibility="collapsed",
                help="Use Ctrl+A to select all, Ctrl+Z to undo"
            )
            
            # Update session state when code changes
            if edited_code != display_code:
                st.session_state.edited_code = edited_code
                st.rerun()
                
        else:
            st.subheader("💻 HTML/CSS Code (Read-only)")
            if st.button("📋 Copy Code", help="Copy code to clipboard"):
                st.code("Code copied! (Use Ctrl+C to copy from the code block below)")
            st.code(display_code, language='html', line_numbers=True)

def generate_python_script(html_content, title="Document"):
    """Generate Python script that can recreate the HTML content"""
    clean_title = title.replace(' ', '_').replace('-', '_').lower()
    
    python_script = f'''#!/usr/bin/env python3
"""
Generated Python script for: {title}
This script recreates the HTML/CSS content and can save it to a file.
"""

def get_html_content():
    """Returns the HTML content as a string"""
    html_content = """{html_content}"""
    return html_content

def save_to_file(filename="{clean_title}.html"):
    """Save the HTML content to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_html_content())
    print(f"HTML content saved to {{filename}}")

def preview_content():
    """Print a preview of the HTML content"""
    content = get_html_content()
    print("HTML Content Preview:")
    print("-" * 50)
    print(content[:500] + "..." if len(content) > 500 else content)
    print("-" * 50)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "save":
            filename = sys.argv[2] if len(sys.argv) > 2 else "{clean_title}.html"
            save_to_file(filename)
        elif sys.argv[1] == "preview":
            preview_content()
        else:
            print("Usage: python script.py [save|preview] [filename]")
    else:
        # Default action: save to file
        save_to_file()
'''
    return python_script

def clean_html_for_download(html_content, remove_download_buttons=True):
    """Clean and structure HTML for download with properly embedded CSS"""
    import re
    
    if remove_download_buttons:
        html_content = re.sub(r'<button[^>]*download-btn[^>]*>.*?</button>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    
    css_pattern = r'<style[^>]*>(.*?)</style>'
    css_matches = re.findall(css_pattern, html_content, re.DOTALL)
    
    # Remove original style tags from content
    html_content = re.sub(css_pattern, '', html_content, flags=re.DOTALL)
    
    # Combine and clean CSS
    combined_css = '\n'.join(css_matches)
    combined_css = re.sub(r'/\*.*?\*/', '', combined_css, flags=re.DOTALL)  # Remove comments
    combined_css = re.sub(r'\s+', ' ', combined_css).strip()  # Minify
    
    if not html_content.strip().startswith('<!DOCTYPE html>'):
        # Extract body content
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
        else:
            body_content = html_content
        
        # Create clean HTML structure with CSS properly embedded
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Downloaded Content</title>
    <style>
{combined_css}
    </style>
</head>
<body>
{body_content}
</body>
</html>"""
    else:
        # Insert CSS into existing HTML structure
        if '<head>' in html_content and combined_css:
            head_end = html_content.find('</head>')
            if head_end != -1:
                html_content = html_content[:head_end] + f'    <style>\n{combined_css}\n    </style>\n' + html_content[head_end:]
    
    return html_content

def generate_pdf_from_html(html_content, title="Document"):
    """Generate PDF from HTML with enhanced CSS rendering"""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib.colors import HexColor, black, blue
        from io import BytesIO
        import re
        from html.parser import HTMLParser
        
        class AdvancedHTMLToPDFParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.content = []
                self.current_text = ""
                self.in_style = False
                self.in_script = False
                self.in_title = False
                self.in_header = False
                self.header_level = 0
                self.in_paragraph = False
                self.text_style = 'normal'
                
            def handle_starttag(self, tag, attrs):
                if tag == 'style':
                    self.in_style = True
                elif tag == 'script':
                    self.in_script = True
                elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    self._flush_current_text()
                    self.in_header = True
                    self.header_level = int(tag[1])
                elif tag == 'title':
                    self.in_title = True
                elif tag == 'p':
                    self._flush_current_text()
                    self.in_paragraph = True
                elif tag in ['strong', 'b']:
                    self.text_style = 'bold'
                elif tag in ['em', 'i']:
                    self.text_style = 'italic'
                elif tag == 'br':
                    self.content.append(('break', ''))
                elif tag == 'hr':
                    self.content.append(('line', ''))
                    
            def handle_endtag(self, tag):
                if tag == 'style':
                    self.in_style = False
                elif tag == 'script':
                    self.in_script = False
                elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    if self.current_text.strip():
                        self.content.append(('header', self.current_text.strip(), self.header_level))
                        self.current_text = ""
                    self.in_header = False
                    self.header_level = 0
                elif tag == 'title':
                    self.in_title = False
                elif tag == 'p':
                    self._flush_current_text()
                    self.in_paragraph = False
                elif tag in ['strong', 'b', 'em', 'i']:
                    self.text_style = 'normal'
                    
            def handle_data(self, data):
                if not self.in_style and not self.in_script and not self.in_title:
                    self.current_text += data
                    
            def _flush_current_text(self):
                if self.current_text.strip():
                    self.content.append(('text', self.current_text.strip(), self.text_style))
                    self.current_text = ""
                    
            def get_content(self):
                self._flush_current_text()
                return self.content
        
        # Create PDF buffer
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=1*inch, bottomMargin=1*inch)
        styles = getSampleStyleSheet()
        story = []
        
        # Enhanced styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=22,
            spaceAfter=30,
            textColor=HexColor('#1a365d'),
            alignment=1,
            fontName='Helvetica-Bold'
        )
        
        header_styles = {
            1: ParagraphStyle('Header1', parent=styles['Heading1'], fontSize=18, spaceAfter=20, textColor=HexColor('#2d3748'), fontName='Helvetica-Bold'),
            2: ParagraphStyle('Header2', parent=styles['Heading2'], fontSize=16, spaceAfter=15, textColor=HexColor('#4a5568'), fontName='Helvetica-Bold'),
            3: ParagraphStyle('Header3', parent=styles['Heading3'], fontSize=14, spaceAfter=12, textColor=HexColor('#4a5568'), fontName='Helvetica-Bold'),
        }
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            textColor=HexColor('#2d3748'),
            leading=16,
            fontName='Helvetica'
        )
        
        bold_style = ParagraphStyle(
            'BoldText',
            parent=body_style,
            fontName='Helvetica-Bold'
        )
        
        # Add title
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 20))
        
        # Parse HTML content
        parser = AdvancedHTMLToPDFParser()
        parser.feed(html_content)
        content_items = parser.get_content()
        
        # Convert parsed content to PDF elements
        for item in content_items:
            if item[0] == 'header':
                level = min(item[2], 3)
                style = header_styles.get(level, header_styles[3])
                story.append(Paragraph(item[1], style))
                story.append(Spacer(1, 10))
            elif item[0] == 'text':
                clean_text = item[1].replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                if clean_text.strip() and len(clean_text.strip()) > 2:
                    text_style = bold_style if len(item) > 2 and item[2] == 'bold' else body_style
                    story.append(Paragraph(clean_text, text_style))
            elif item[0] == 'break':
                story.append(Spacer(1, 8))
            elif item[0] == 'line':
                story.append(Spacer(1, 12))
        
        # Fallback if no content parsed
        if not content_items:
            story.append(Paragraph("This document contains primarily visual content. Please view the HTML version for the complete experience.", body_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
        
    except ImportError:
        return None
    except Exception as e:
        st.error(f"PDF generation error: {str(e)}")
        return None

# --- DOWNLOAD BUTTONS ---
if example_info:
    st.markdown("---")
    
    if example_info.get('pdf_enabled') or (isinstance(example_info.get('pdf_enabled'), str) and example_info.get('pdf_enabled').lower() == 'true'):
        col1, col2 = st.columns([1, 1])
    else:
        col1, col2 = st.columns([1, 1])
    
    with col1:
        # PDF download (only for PDF-enabled examples)
        if example_info.get('pdf_enabled') or (isinstance(example_info.get('pdf_enabled'), str) and example_info.get('pdf_enabled').lower() == 'true'):
            pdf_data = generate_pdf_from_html(current_code, example_info['title'])
            if pdf_data:
                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_data,
                    file_name=f"{example_info['title'].replace(' ', '_')}.pdf",
                    mime="application/pdf",
                    help="Download as formatted PDF with styling applied"
                )
            else:
                if st.button("📄 Download PDF"):
                    st.error("PDF generation requires reportlab package")
        else:
            st.write("")  # Empty space for alignment
    
    with col2:
        clean_html = clean_html_for_download(current_code, remove_download_buttons=True)
        st.download_button(
            label="💾 Download HTML",
            data=clean_html,
            file_name=f"{example_info['title'].replace(' ', '_')}.html",
            mime="text/html",
            help="Download clean HTML with embedded CSS styling (no raw code visible)"
        )

# --- STATUS BAR ---
if example_info:
    st.markdown("---")
    
    # Show download buttons for all examples (not just PDF-enabled ones)
    if example_info.get('pdf_enabled') or (isinstance(example_info.get('pdf_enabled'), str) and example_info.get('pdf_enabled').lower() == 'true'):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    else:
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# --- STATUS BAR ---
st.markdown("---")
status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.metric("Selected Item", selected_number)

with status_col2:
    if data_source == "📋 Demo Examples" and example_info:
        st.metric("Category", example_info['category'])
    else:
        mode_status = "✏️ Edit Mode" if edit_mode else "👁️ View Mode"
        st.metric("Current Mode", mode_status)

with status_col3:
    if data_source == "📋 Demo Examples":
        st.metric("Total Examples", len(DEMO_EXAMPLES))
    else:
        try:
            total_entries = len(df) if 'df' in locals() and not df.empty else 0
            st.metric("Total Entries", total_entries)
        except:
            st.metric("Total Entries", "N/A")

with status_col4:
    preview_status = "🌐 Live" if live_preview else "📱 Hidden"
    st.metric("Preview Status", preview_status)

# --- DEMO EXAMPLES INFO ---
if data_source == "📋 Demo Examples":
    with st.expander("📋 Demo Examples Overview", expanded=False):
        st.markdown("""
        **8 Professional Demo Examples Available:**
        
        1. **Newsletter Template** - Real Estate Weekly (PDF Downloadable)
        2. **Landing Page** - CreditPro Financial Solutions  
        3. **Corporate Website** - Premier Realty Agency
        4. **Streamlit Dashboard** - Business Analytics Interface
        5. **Business Letter** - Credit Application Response (PDF Downloadable)
        6. **Email Sequence** - Real Estate Lead Nurturing (7 emails)
        7. **Professional Invoice** - Business Services (PDF Downloadable)
        8. **Business Contract** - Real Estate Purchase Agreement (PDF Downloadable)
        
        **Features:**
        - Professional designs with real business content
        - Credit, real estate, and business themes
        - PDF downloadable documents where applicable
        - Responsive layouts and modern styling
        - Ready-to-use templates for various business needs
        """)

# --- INSTRUCTIONS ---
with st.expander("📖 Instructions & Tips", expanded=False):
    st.markdown(
        """
        **How to use this enhanced code viewer:**
        
        **Data Sources:**
        - **Demo Examples**: 8 professional templates ready to use
        - **Google Sheets**: Load custom code from your spreadsheet
        
        **Display Controls:**
        - **Live Preview**: View rendered HTML/CSS (ON by default)
        - **Show Code Panel**: Display code editor/viewer (OFF by default for cleaner view)
        - **Edit Mode**: Enable real-time code editing
        
        **Enhanced Features:**
        - **Category Filtering**: Filter demo examples by type
        - **Better Defaults**: Live preview on, code off for immediate visual impact
        - **Larger Preview**: Increased height for better viewing experience
        - **Professional Templates**: Real business content, not placeholder text
        - **PDF Downloads**: Simulated download functionality for documents
        
        **Tips:**
        - Start with live preview to see the design immediately
        - Enable code panel only when you need to edit or study the code
        - Use demo examples for inspiration and starting points
        - Edit mode provides real-time preview updates
        """
    )

    st.markdown(
        """
        **Google Sheets Structure:**
        Your Google Sheet should have these columns:
        - **Number** (required): Unique identifier
        - **Code** (required): HTML/CSS content
        - **Title** (optional): Display name
        - **Category** (optional): Group classification
        - **Description** (optional): Brief description
        - **PDF_Enabled** (optional): true/false for PDF download capability
        
        **Real Downloads:**
        - **PDF Downloads**: Generate actual PDF files from HTML content
        - **HTML Downloads**: Save HTML/CSS code directly
        - **Streamlit Integration**: Uses native download functionality
        """
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.8em;'>"
    "🚀 Enhanced Code Viewer | 8 Professional Demo Examples | Real-time Editing | PDF Downloads"
    "</div>", 
    unsafe_allow_html=True
)


st.markdown("""
<script>
function downloadPDF() {
    alert('PDF download feature would be implemented with server-side PDF generation');
}
</script>
""", unsafe_allow_html=True)
