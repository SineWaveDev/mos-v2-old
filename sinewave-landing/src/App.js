import React from 'react';
import './App.css';
import logo from "./logo.jpg"; // Adjusted path for the logo

const App = () => {
  return (
    <div className="app-container">
      {/* Wave Background */}
      <div className="wave-container">
        <div className="wave wave1"></div>
        <div className="wave wave2"></div>
        <div className="wave wave3"></div>
      </div>

      <header className="header">
        <img src={logo} alt="Sinewave Logo" className="logo" />
        <button 
          className="callback-button" 
          onClick={() => window.open('https://www.google.com/maps/place/Sinewave/@18.5050673,73.8027803,11896m/data=!3m2!1e3!5s0x3bc2c07a3f60a131:0xea24277816c3ff0e!4m8!3m7!1s0x3bc2c101069d01eb:0x76087e3a7e141fbc!8m2!3d18.4823815!4d73.8962535!9m1!1b1!16s%2Fg%2F1tsjc383?authuser=0&entry=ttu&g_ep=EgoyMDI1MDExNC4wIKXMDSoASAFQAw%3D%3D', '_blank')}
        >
          See Our Reviews <span className="right-arrow">→</span>
        </button>
        <h1 className="title">Empowering Your Business with Cutting-Edge Tax Solutions</h1>
        <p className="subtitle">
          Beyond Income Tax: A Comprehensive Financial Solution.
        </p>
      </header>

      <div className="product-container">
      <section className="product">
        <h2 className="product-title">Taxbase - Income Tax Software</h2>
        <p className="product-description">
          Comprehensive Tax Solution: All-in-one ERP solution for tax professionals, covering income tax computation, return filing, and office management.
        </p>
        <h3 className="features-title">Key Features</h3>
        <ul className="benefits-list">
          <li>
            <span className="feature-icon"></span>→ Auto-login for e-filing, tax payments, and acknowledgments.
          </li>
          <li>
            <span className="feature-icon"></span>→ Effortless advance tax calculations with reminders.
          </li>
          <li>
            <span className="feature-icon"></span>→ E-file audit forms like 3CA/3CD, 3CB/3CD, 3CEB easily.
          </li>
          <li>
            <span className="feature-icon"></span>→ Simplified calculations with stock and mutual fund libraries.
          </li>
          <li>
            <span className="feature-icon"></span>→ Auto-updated dashboards for TDS/TCS preparation and filing.
          </li>
          <li>
            <span className="feature-icon"></span>→ Personalized notifications, tax calculators, and branded mobile app.
          </li>
          <li>
            <span className="feature-icon"></span>→ Track ITR status, refunds, and notices in real-time.
          </li>
          <li>
            <span className="feature-icon"></span>→ Organize client documents with alerts for pending items.
          </li>
          <li>
            <span className="feature-icon"></span>→ Manage client relationships with SMS, email, and app notifications.
          </li>
        </ul>
        <p><strong>💰 Pricing:</strong></p>
        <ul className="pricing-list">
          <li className="old-price">❌Regular Price: ₹12000/- + 18% Gst</li>
          <li className="new-price">✅Discount Price: ₹10000/- + 18% Gst</li>
        </ul>

        <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*utn0p2*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*utn0p2*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
      </section>


      <section className="product">
        <h2 className="product-title">GST Pro - GST Software</h2>
        <p className="product-description">
          Simplified GST Return Filing: Easily file GSTR-1, GSTR-2, GSTR-3B, and GSTR-4 with automated, error-free calculations for timely compliance.
        </p>
        <h3 className="features-title">Key Features</h3>
        <ul className="benefits-list">
          <li><span className="feature-icon"></span>→ Single clicks download GSTR 1, 2A, 2B & GSTR 3B</li>
          <li><span className="feature-icon"></span>→	Facility to view JSON uploading error status for GSTR 1</li>
          <li><span className="feature-icon"></span>→	Annual reconciliation of Sales with GSTR1, GSTR1 Portal & GSTR 3B</li>
          <li><span className="feature-icon"></span>→	Annual reconciliation of ITC with Purchases, 2A, 2B & GSTR 3B</li>
          <li><span className="feature-icon"></span>→	Facility to generate E-Way Bill & E-Invoice</li>
          <li><span className="feature-icon"></span>→	You can view summary details of the selected dealer on the home screen with return filing details, various ledger balances with short cut keys</li>
          <li><span className="feature-icon"></span>→	Single Click “Prefill” to get portal Static information.</li>
          <li><span className="feature-icon"></span>→	API facility to upload & download various details.</li>
          <li><span className="feature-icon"></span>→	Facility to import Tally data import in Sales & Purchase</li>
        </ul>
        <p><strong>Pricing:</strong></p>
        <ul className="pricing-list">
          <li className="old-price">❌ Regular Price: ₹12000/- +18% Gst</li>
          <li className="new-price">✅ Discount Price: ₹10000/- +18% Gst</li>
        </ul>
        <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/GST/GST-download.aspx?_gl=1*1fp0lr5*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/GST/GST-download.aspx?_gl=1*1fp0lr5*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
      </section>


        {/* New Product Section for Paywhiz Pro */}
        <section className="product">
          <h2 className="product-title">Paywhiz Pro - Advanced HR & Payroll Software</h2>
          <p className="product-description">
            Take your HR and payroll management to the next level with Paywhiz Pro. Automate attendance, salary processing, and ensure compliance with ease.
          </p>
          <h3 className="features-title">Key Features </h3>
          <ul className="benefits-list">
            <li><span className="feature-icon"></span>→	It is a combination of three modules as Payroll, Income Tax and TDS.</li>
            <li><span className="feature-icon"></span>→	Auto data sync facility from Sinewave’s Attendance software for salary</li>
            <li><span className="feature-icon"></span>→	No limit for companies and employees.</li>
            <li><span className="feature-icon"></span>→	Facility to generate Auto Salary for all employees</li>
            <li><span className="feature-icon"></span>→	Various reports like monthly, annually, periodic and miscellaneous </li>
            <li><span className="feature-icon"></span>→	Customized payroll register available.</li>
            <li><span className="feature-icon"></span>→ Facility to import data from biomatrix machine for salary processing</li>
            <li><span className="feature-icon"></span>→	Facility to import data from Excel for salary processing.</li>
            <li><span className="feature-icon"></span>→	Auto computation of Tax, based on salary details.</li>
          </ul>
          <p><strong>Pricing:</strong></p>
          <ul className="pricing-list">
            <li className="old-price">❌ Regular Price: ₹60000/- +18% Gst</li>
            <li className="new-price">✅ Discount Price: ₹50000/- +18% Gst</li>
          </ul>
          <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1wprg3q*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1wprg3q*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        </section>


        {/* New Product Section for TDS Pro */}
        <section className="product">
          <h2 className="product-title">TDS Pro - Advanced TDS/TCS Management Software</h2>
          <p className="product-description">
            Simplify your TDS/TCS processes with TDS Pro. Automate calculations, ensure compliance, and file returns effortlessly.
          </p>
          <h3 className="features-title">Key Features</h3>
          <ul className="benefits-list">
            <li><span className="feature-icon"></span>→	Auto Computes TDS Deduction And Generates ITR For Employees</li>
            <li><span className="feature-icon"></span>→	Section wise E- Payment facility for Online or Over the Counter facility </li>
            <li><span className="feature-icon"></span>→	Return Record Register (Filed / Not Filed)</li>
            <li><span className="feature-icon"></span>→	Online Services For TDS And Employee</li>
            <li><span className="feature-icon"></span>→	Auto Fetch – TDS Justification From Traces</li>
            <li><span className="feature-icon"></span>→	Prepare/ Generate Form 15G/15H And E-File</li>
            <li><span className="feature-icon"></span>→	Notice Management</li>
            <li><span className="feature-icon"></span>→	User Manual / E-Guide & FAQ’s Incorporated</li>
            <li><span className="feature-icon"></span>→	It Covers TCS Working Also</li>
            <li><span className="feature-icon"></span>→	Lower/Higher/No Deduction Management U/S 197</li>
          </ul>
          <p><strong>Pricing:</strong></p>
          <ul className="pricing-list">
            <li className="old-price">❌ Regular Price: ₹9000/- + 18%Gst</li>
            <li className="new-price">✅ Discount Price: ₹7500/- + 18%Gst</li>
          </ul>
          <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/TDS/TDS-download.aspx?_gl=1*xwgqlg*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/TDS/TDS-download.aspx?_gl=1*xwgqlg*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        </section>


        {/* New Product Section for Taxbase Signer Software */}
        <section className="product">
          <h2 className="product-title">Taxbase Signer Software – Simplify Your Digital Signing Needs</h2>
          <p className="product-description">
            Effortlessly sign and manage your documents with Taxbase Signer Software, designed to enhance security, compliance, and operational efficiency.
          </p>
          <h3 className="features-title">Key Features</h3>
          <ul className="benefits-list">
            <li><span className="feature-icon"></span>→	Digitally sign PDF documents and other files using DSC tokens from authorized vendors in India, ensuring authenticity and security.</li>
            <li><span className="feature-icon"></span>→	Save time and streamline operations by digitally signing multiple documents in bulk.</li>
            <li><span className="feature-icon"></span>→	Personalize your digital signatures by choosing the logo, page, position, and location for a professional appearance.</li>
            <li><span className="feature-icon"></span>→	Enhance document integrity with time-stamped signatures supporting LTV, ensuring compliance and tamper-proof security.</li>
            <li><span className="feature-icon"></span>→	Compatible with smart card and qualified certificates for broad industry application.</li>
            <li><span className="feature-icon"></span>→	Fully adheres to Indian IT Act 2000 and PKCS#7 standards, ensuring legal and industry compliance for digital signatures.</li>
            <li><span className="feature-icon"></span>→	Eliminate manual effort with automated signing features that increase efficiency for organizations.</li>
            <li><span className="feature-icon"></span>→	Enjoy a user-friendly interface with step-by-step guidance and automated folder creation for signed files.</li>
            <li><span className="feature-icon"></span>→	Supports signing of various documents, including invoices, bills, contracts, and other critical files, catering to diverse business needs.</li>
            <li><span className="feature-icon"></span>→	Automatically organizes signed files into a designated destination folder for efficient file management and easy retrieval.</li>
          </ul>
          <p><strong>Pricing:</strong></p>
          <ul className="pricing-list">
            <li className="old-price">❌ Standard Price: ₹10000/- +18% Gst</li>
            <li className="new-price">✅ Limited-Time Offer: ₹8000/- +18% Gst</li>
          </ul>
          <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/taxbase-signer/TBsigner-download.aspx?_gl=1*u3ggp4*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/taxbase-signer/TBsigner-download.aspx?_gl=1*u3ggp4*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        </section>



        {/* New Product Section for Team Control Software */}
        <section className="product">
          <h2 className="product-title">Team Control Software – Optimize Workforce Management Effortlessly</h2>
          <p className="product-description">
            Streamline employee management, attendance tracking, and payroll integration with Team Control Software, a comprehensive solution for modern HR needs.
          </p>
          <h3 className="features-title">Key Features</h3>
          <ul className="benefits-list">
            <li><span className="feature-icon"></span>→	Organize employees by designation, department, and shift with intuitive tools for managing shift rules and schedules.</li>
            <li><span className="feature-icon"></span>→	Generate daily, monthly, and summary attendance reports, including details on present, absent, late, and half-day entries.</li>
            <li><span className="feature-icon"></span>→	Simplify leave applications, approvals, and rejections with real-time tracking and automated notifications.</li>
            <li><span className="feature-icon"></span>→	Monitor workforce metrics like attendance, leave balances, and shift compliance through a user-friendly, real-time dashboard.</li>
            <li><span className="feature-icon"></span>→	Manage attendance flexibly with manual entry options or biometric integration for accurate tracking.</li>
            <li><span className="feature-icon"></span>→	Enable employees to view attendance, leave statuses, and reports anytime through the dedicated Android app.</li>
            <li><span className="feature-icon"></span>→	Synchronize seamlessly with Paywhiz software to provide employees with payslips, salary statements, and Form 16.</li>
            <li><span className="feature-icon"></span>→	Generate tailored reports using advanced filters and search options for in-depth analysis of attendance, leave, and payroll data.</li>
            <li><span className="feature-icon"></span>→	Boost productivity for field employees with tools for self-entry, pre-approval processes, and supervisor allocations.</li>
          </ul>
          <p><strong>Pricing Details:</strong></p>
          <ul className="pricing-list">
            <li className="old-price">❌ Standard Price: ₹4500</li>
            <li className="new-price">✅ Limited-Time Offer: ₹4000</li>
          </ul>
          <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/teamcontrol/TC_Free_Register.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/teamcontrol/TC_Free_Register.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        </section>




        {/* New Product Section for MOS */}
        <section className="product">
          <h2 className="product-title">MOS - Portfolio Management & Tax Computation Software</h2>
          <p className="product-description">
            Efficiently manage your investments with MOS. Track stocks, mutual funds, and more while automating capital gains calculations for stress-free tax compliance.
          </p>
          <h3 className="features-title">Key Features</h3>
          <ul className="benefits-list">
            <li><span className="feature-icon"></span>→	Manage investments across stocks, mutual funds, futures & options, and day trading with ease.</li>
            <li><span className="feature-icon"></span>→	Instantly view portfolio values and returns at both script and overall portfolio levels.</li>
            <li><span className="feature-icon"></span>→	Sync data between cloud and Android platforms for on-the-go access to your portfolio.</li>
            <li><span className="feature-icon"></span>→	Automatically calculate short-term and long-term capital gains along with applicable taxes.</li>
            <li><span className="feature-icon"></span>→	Generate comprehensive profit/loss reports, script-specific profits, stock holdings, and speculation analysis with graphical insights.</li>
            <li><span className="feature-icon"></span>→	Simplify stock management with automatic calculation of closing stock, average rates, and market value retrieval.</li>
            <li><span className="feature-icon"></span>→	Import MOS data into Taxbase for streamlined tax computation and filing.</li>
            <li><span className="feature-icon"></span>→	Monitor your portfolio and view reports via the MOS Android app.</li>
            <li><span className="feature-icon"></span>→	Export transaction reports in XLS format for personalized analysis and strategic decision-making.</li>
          </ul>
          <p><strong>Pricing:</strong></p>
          <ul className="pricing-list">
            <li className="old-price">❌ Regular Price: ₹6000</li>
            <li className="new-price">✅ Discount Price: ₹5000</li>
          </ul>
          <div className="button-group">
          <a href="https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx" className="button buy-now" target="_blank" rel="noopener noreferrer">
            Buy Now
          </a>
          <button 
            className="button demo-button" 
            onClick={() => {
              window.location.href = 'https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        </section>

        </div>
   {/* Footer */}
   <footer className="footer">
        <div className="footer-content">
          <div className="footer-section">
            <h3>About Us</h3>
            <p>Sinewave Computer Services Pvt. Ltd. (ISO 9001-2015 Certified) is 36 years old income tax and HR solutions software development company situated in Pune, Maharashtra, India. We are catering to 20,000+ customer base across India.</p>
          </div>
          <div className="footer-section">
            <h3>Taxation Products</h3>
            <ul>
              <li>TaxbasePro</li>
              <li>Taxbase GSTPro</li>
              <li>Paywhiz</li>
              <li>TDSPro</li>
              <li>Form 3CD</li>
              <li>TeamControl</li>
            </ul>
          </div>
          <div className="footer-section">
            <h3>Our Service Offerings</h3>
            <ul>
              <li>DSC (Digital Signature)</li>
              <li>Partner With Us</li>
              <li>Become a Channel Partner</li>
              <li>Customer Support</li>
            </ul>
          </div>
          <div className="footer-section">
            <h3>Contact Us</h3>
            <p>For Support, call us at <strong>020 4909 1000</strong></p>
            <p><a href="tel:+91-02049091000">Click to Register Call Back</a></p>
            <p>For escalation, please contact us on <strong>020 4909 1000</strong> or <strong>09637769351</strong> or write us at <a href="mailto:crm@sinewave.co.in">crm@sinewave.co.in</a></p>
            <p>For DSC Support: <strong>099230 01785</strong></p>
            <p>Not satisfied with the support provided? What’s App the customer ID and issue on (Executive Assistant/Director’s Office).</p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2025 Sinewave Computer Services Pvt. Ltd. All Rights Reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default App;