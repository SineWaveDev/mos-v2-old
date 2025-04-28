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
       {/* New Announcement Line */}
       <p className="announcement">
        <strong>Avail incredible discounts</strong> on your favorite software (valid until <em>31st March 2025</em>).<br />
        <strong>Coming Soon: AI Powered Softwares to accelerate your Legal Research and Practice!</strong>
      </p>


      <div className="product-container">
        {/* Product Box */}
        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">Taxbase - Income Tax Software</h2>
            <p className="product-description">Comprehensive Tax Solution: All-in-one ERP solution for tax professionals, covering income tax computation, return filing, and office management.</p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Special Offer:</strong> With Taxbase, you get TDS Pro software absolutely free!</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Discount Price: ₹10,000/- + 18% GST</p>
              <p className="old-price">❌ Regular Price: ₹15,000/- + 18% GST</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Includes TDSpro software</strong> </li>
            <li><strong>* Auto-login</strong></li>
            <li><strong>* Effortless advance tax calculations</strong> </li>
            <li><strong>* E-file audit forms</strong> </li>
            <li><strong>* Simplified calculations</strong></li>
            <li><strong>* Auto-updated dashboards</strong> </li>
            <li><strong>* Personalized notifications</strong>.</li>
            <li><strong>* Track ITR status, refunds, and notices</strong></li>
            <li><strong>* Organize client documents</strong></li>
            <li><strong>* Manage client relationships</strong></li>
          </ul>

          <a 
            href="https://sinewave.co.in/taxbasepro-itr/" 
            className="read-more small-text" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>
          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*utn0p2*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href =
                  'https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*utn0p2*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
              }}
            >
              Get Demo
            </button>

            
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>
        



        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">GST Pro - GST Software</h2>
            <p className="product-description">Simplified GST Return Filing: Easily file GSTR-1, GSTR-2, GSTR-3B, and GSTR-4 with automated, error-free calculations for timely compliance.</p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Special Offer:</strong> Simplified GST Return Filing with automation for timely compliance!</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Discount Price: ₹8,000/- + 18% GST</p>
              <p className="old-price">❌ Regular Price: ₹12,000/- + 18% GST</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Single click download</strong></li>
            <li><strong>* View JSON upload errors</strong></li>
            <li><strong>* Annual reconciliation</strong></li>
            <li><strong>* ITC reconciliation</strong></li>
            <li><strong>* Generate E-Way Bills & E-Invoices</strong></li>
            <li><strong>* Summary dashboard</strong></li>
            <li><strong>* Single click “Prefill”</strong></li>
            <li><strong>* API support</strong></li>
            <li><strong>* Import data</strong> </li>
            <li><strong>* Easy e-filing</strong></li>
          </ul>

          <a 
            href="https://sinewave.co.in/best-gst-software-india/" 
            className="read-more" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>

          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/GST/GST-download.aspx?_gl=1*1fp0lr5*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href =
                  'https://crm.sinewave.co.in/products/GST/GST-download.aspx?_gl=1*1fp0lr5*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
              }}
            >
              Get Demo
            </button>
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>




        {/* New Product Section for Paywhiz Pro */}
        <section className="product-box">
        <div className="product-header">
          <h2 className="product-title">Paywhiz Pro - Advanced HR & Payroll Software</h2>
          <p className="product-description">Take your HR and payroll management to the next level with Paywhiz Pro. Automate attendance, salary processing, and ensure compliance with ease.</p>
          
          {/* Highlighting Offers */}
          <div className="highlight-offer">
            <p><strong>🎉 Special Offer:</strong> With Paywhiz Pro, you get  Payroll, Income Tax and TDS software absolutely free! </p>
          </div>
          <div className="price-box">
            <p className="new-price">✅ Discount Price: ₹50,000/- + 18% GST</p>
            <p className="old-price">❌ Regular Price: ₹60,000/- + 18% GST</p>
          </div>
        </div>

        <h3 className="features-title">Key Features</h3>
        <ul className="features-list">
          <li><strong>* Includes three modules</strong></li>
          <li><strong>* Auto data sync</strong></li>
          <li><strong>* No limits</strong></li>
          <li><strong>* Auto Salary generation</strong></li>
          <li><strong>* Generate reports</strong></li>
          <li><strong>* Customized payroll register</strong></li>
          <li><strong>* Biomatrix integration</strong></li>
          <li><strong>* Excel import support</strong></li>
          <li><strong>* Auto computation</strong></li>
        </ul>

        <a 
            href="https://sinewave.co.in/paywhiz-pro-new/" 
            className="read-more" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>

        <div className="button-group">
          <a
            href="https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1wprg3q*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
            className="button buy-now"
            target="_blank"
            rel="noopener noreferrer"
          >
            Buy Now
          </a>
          <button
            className="button demo-button"
            onClick={() => {
              window.location.href =
                'https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1wprg3q*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
            }}
          >
            Get Demo
          </button>
        </div>
        <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
      </section>


        {/* New Product Section for TDS Pro */}
        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">TDS Pro - Advanced TDS/TCS Management Software</h2>
            <p className="product-description">Simplify your TDS/TCS processes with TDS Pro. Automate calculations, ensure compliance, and file returns effortlessly.</p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Special Offer:</strong> Simplify your TDS and TCS management with TDS Pro at a discounted price!</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Discount Price: ₹5,000/- + 18% GST</p>
              <p className="old-price">❌ Regular Price: ₹7,500/- + 18% GST</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Auto Computes TDS</strong></li>
            <li><strong>* Section wise E-Payment</strong> </li>
            <li><strong>* Return Record Register</strong></li>
            <li><strong>* Online Services</strong></li>
            <li><strong>* Auto Fetch TDS Justification</strong></li>
            <li><strong>* Prepare & E-File Forms</strong></li>
            <li><strong>* Notice Management</strong></li>
            <li><strong>* User Manual & FAQ</strong></li>
            <li><strong>* TCS Coverage</strong></li>
            <li><strong>* Section 197 Management</strong></li>
          </ul>

          <a 
            href="https://sinewave.co.in/tds-pro-tds-calculation-software-india/" 
            className="read-more" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>

          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/TDS/TDS-download.aspx?_gl=1*xwgqlg*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href =
                  'https://crm.sinewave.co.in/products/TDS/TDS-download.aspx?_gl=1*xwgqlg*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
              }}
            >
              Get Demo
            </button>
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>


        {/* New Product Section for Taxbase Signer Software */}
        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">Taxbase Signer Software – Simplify Your Digital Signing Needs</h2>
            <p className="product-description">Effortlessly sign and manage your documents with Taxbase Signer Software, designed to enhance security, compliance, and operational efficiency.</p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Limited-Time Offer:</strong> Get Taxbase Signer at a discounted price for a seamless digital signing experience!</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Limited-Time Offer: ₹8,000/- + 18% GST</p>
              <p className="old-price">❌ Standard Price: ₹10,000/- + 18% GST</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Digitally Sign Documents</strong></li>
            <li><strong>* Bulk Signing</strong></li>
            <li><strong>* Personalized Signatures</strong></li>
            <li><strong>* Enhanced Document Integrity</strong></li>
            <li><strong>* Wide Compatibility</strong></li>
            <li><strong>* Legal Compliance</strong> </li>
            <li><strong>* Automated Signing</strong> </li>
            <li><strong>* User-Friendly Interface</strong></li>
            <li><strong>* Supports Various Documents</strong> </li>
            <li><strong>* Efficient File Management</strong></li>
          </ul>

          <a 
            href="https://sinewave.co.in/taxbase-signer-india/" 
            className="read-more" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>

          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/taxbase-signer/TBsigner-download.aspx?_gl=1*u3ggp4*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href =
                  'https://crm.sinewave.co.in/products/taxbase-signer/TBsigner-download.aspx?_gl=1*u3ggp4*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
              }}
            >
              Get Demo
            </button>
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>


        {/* New Product Section for MOS */}
        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">MOS - Portfolio Management & Tax Computation Software</h2>
            <p className="product-description">Simplified GST Return Filing: Easily file GSTR-1, GSTR-2, GSTR-3B, and GSTR-4 with automated, error-free calculations for timely compliance.</p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Limited-Time Offer:</strong> Get MOS at a discounted price for efficient investment management and tax computation!</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Discount Price: ₹5,000/- + 18% GST</p>
              <p className="old-price">❌ Regular Price: ₹6,000/- + 18% GST</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Investment Management</strong></li>
            <li><strong>* Portfolio Insights</strong> </li>
            <li><strong>* Cloud Sync</strong></li>
            <li><strong>* Tax Automation</strong> </li>
            <li><strong>* Reporting Tools</strong></li>
            <li><strong>* Stock Management</strong></li>
            <li><strong>* Integration with Taxbase</strong></li>
            <li><strong>* Mobile App Access</strong></li>
            <li><strong>* Custom Reporting</strong></li>
          </ul>

          <a 
            href="https://sinewave.co.in/taxbasepro-itr/" 
            className="read-more" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>

          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href =
                  'https://crm.sinewave.co.in/products/taxbase/taxbase-download.aspx?_gl=1*1qpf33e*_gcl_au*MTAzNDUxNjQ5OC4xNzM3MzU5NjUx';
              }}
            >
              Get Demo
            </button>
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>

        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">TeamNest - HR and Payroll Software</h2>
            <p className="product-description">
              Comprehensive HR and Payroll Solution: TeamNest is designed to handle every HR and payroll use case, with a focus on efficiency and user-friendly features.
            </p>
            {/* Highlighting Offers */}
            <div className="highlight-offer">
              <p><strong>🎉 Special Offer:</strong> OFFER 50% DISCOUNT for 1st 100 registrations the price as OFFER PROCE Rs 1/- (Terms & Conditions Apply)</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Discount Price  Rs 1/- per user per day....only for 1st 100 applicants. Actual price Rs 2/- per user per day. Terms and Conditions Apply (CLOUD BASED HRMS)</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Attendance Management</strong></li>
            <li><strong>* Leave Tracking</strong></li>
            <li><strong>* Expense Management</strong></li>
            <li><strong>* Payroll Processing</strong></li>
            <li><strong>* Compliance Management</strong></li>
            <li><strong>* Employee Onboarding</strong></li>
            <li><strong>* Exit Management</strong></li>
            <li><strong>* Performance Management</strong></li>
            <li><strong>* Maximum 15 employees</strong></li>
            <li><strong>* Free for 1 year</strong></li>
            <li><strong>* CA membership # compulsory for availing this offer</strong></li>
          </ul>

        

          <a 
            href="https://crm.sinewave.co.in/" 
            className="read-more small-text" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Read More
          </a>
          <div className="button-group">
            <a
              href="https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1jn9a57*_gcl_au*MjAzMTk0NjMwOC4xNzM3Nzk5MTAz"
              className="button buy-now"
              target="_blank"
              rel="noopener noreferrer"
            >
              Buy Now
            </a>
            <button
              className="button demo-button"
              onClick={() => {
                window.location.href = 'https://crm.sinewave.co.in/products/PaywhizPro/paywhizPro-download.aspx?_gl=1*1jn9a57*_gcl_au*MjAzMTk0NjMwOC4xNzM3Nzk5MTAz';
              }}
            >
              Get Demo
            </button>
          </div>
          <p className="contact-details">
            To buy this product, contact us at <strong>8600352217</strong> or email <strong>crm@sinewave.co.in</strong>.
          </p>
        </section>


        <section className="product-box">
          <div className="product-header">
            <h2 className="product-title">COMING SOON</h2>
            <p className="product-description">
              Empowering legal professionals with AI-driven research, document analysis, and drafting tools, automating critical parts of their professional workflow.
            </p>
            {/* Highlighting Features */}
            <div className="highlight-offer">
              <p><strong>🎉 Coming Soon:</strong> AI driven Platform for Legal Research , Analysis & Drafting.</p>
            </div>
            <div className="price-box">
              <p className="new-price">✅ Transparent and Explainable AI for Legal Practice</p>
              <p className="old-price">❌ No Compromises on Accuracy or Reliability</p>
            </div>
          </div>

          <h3 className="features-title">Key Features</h3>
          <ul className="features-list">
            <li><strong>* Ask:</strong> Get concise answers to legal queries with Explainable AI (XAI) and supporting citations.</li>
            <li><strong>* Interact:</strong> Upload multiple legal documents for summaries and cross-document insights.</li>
            <li><strong>* Draft:</strong> Effortlessly draft appeals, orders, contracts, and more.</li>
            <li><strong>* Trained on:</strong> 10 million legal documents and over 20 billion tokens.</li>
            <li><strong>* Foundation Models:</strong> Tested with models ranging from 7 to 70 billion parameters.</li>
            <li><strong>* Transparent AI:</strong> Provides clear explanations and source references for additional trust.</li>
          </ul>
          <ul className="features-list">
            <li><strong>* Above Key Features
            ...just say COMING SOON</strong></li>
            
          </ul>

          <div className="button-group">
            {/* Buttons disabled */}
            <button className="button disabled-button" disabled>
              Buy Now
            </button>
            <button className="button disabled-button" disabled>
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