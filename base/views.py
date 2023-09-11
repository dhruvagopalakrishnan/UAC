import datetime
from uac.settings import RAZOR_API_KEY, RAZOR_API_SECRET_KEY,EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.shortcuts import redirect, render
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from base import models, forms
from .models import esfn, fsfn
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import SubscribersForm
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from .forms import SaveTransport
from django.core.mail import send_mail
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render



html_mailer = """\
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title></title>
  <script>
    
  </script>
    <style type="text/css">
      @media only screen and (min-width: 520px) {{
  .u-row {{
    width: 500px !important;
  }}
  .u-row .u-col {{
    vertical-align: top;
  }}

  .u-row .u-col-100 {{
    width: 500px !important;
  }}

}}

@media (max-width: 520px) {{
  .u-row-container {{
    max-width: 100% !important;
    padding-left: 0px !important;
    padding-right: 0px !important;
  }}
  .u-row .u-col {{
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
  }}
  .u-row {{
    width: calc(100% - 40px) !important;
  }}
  .u-col {{
    width: 100% !important;
  }}
  .u-col > div {{
    margin: 0 auto;
  }}
}}
body {{
  margin: 0;
  padding: 0;
}}

table,
tr,
td {{
  vertical-align: top;
  border-collapse: collapse;
}}

.ie-container table,
.mso-container table {{
  table-layout: fixed;
}}

* {{
  line-height: inherit;
}}

a[x-apple-data-detectors='true'] {{
  color: inherit !important;
  text-decoration: none !important;
}}
table, td {{ color: #ffffff; }} </style>
</head>

<body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #000000;color: #ffffff">

  <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #000000;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    
    

<div class="u-row-container" style="padding: 0px;background-color: transparent">
  <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      
      

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    <strong><em>UAC - YOUR BOOKINGS.</em></strong>
  </h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    Name: {NAME}
  </h1>
  <img align="center" border="0" src="space.jpeg" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 480px;" width="480"/>
      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    From: {FROM}
  </h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    To: {TO}
  </h1> 
      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left"> 
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    Contact: {CONTACT}
  </h1>
      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left"> 
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;">
    Flight ID: {FID}
  </h1>
      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding-right: 0px;padding-left: 0px;" align="center">
    </td>
  </tr>
</table>
      </td>
    </tr>
  </tbody>
</table>  
  </div>
</div>
    </div>
  </div>
</div>
</body>
</html>
"""

second_mailer = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>

  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <title></title>
  
    <style type="text/css">
      @media only screen and (min-width: 520px) {{
  .u-row {{
    width: 500px !important;
  }}
  .u-row .u-col {{
    vertical-align: top;
  }}

  .u-row .u-col-100 {{
    width: 500px !important;
  }}

}}

@media (max-width: 520px) {{
  .u-row-container {{
    max-width: 100% !important;
    padding-left: 0px !important;
    padding-right: 0px !important;
  }}
  .u-row .u-col {{
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
  }}
  .u-row {{
    width: 100% !important;
  }}
  .u-col {{
    width: 100% !important;
  }}
  .u-col > div {{
    margin: 0 auto;
  }}
}}
body {{
  margin: 0;
  padding: 0;
}}

table,
tr,
td {{
  vertical-align: top;
  border-collapse: collapse;
}}

.ie-container table,
.mso-container table {{
  table-layout: fixed;
}}

* {{
  line-height: inherit;
}}

a[x-apple-data-detectors='true'] {{
  color: inherit !important;
  text-decoration: none !important;
}}

table, td {{ color: #ffffff; }} </style>
  
  

<link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,700&display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->

</head>

<body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #000000;color: #ffffff">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #000000;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #000000;"><![endif]-->
    

<div class="u-row-container" style="padding: 0px;background-color: transparent">
  <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="500" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
  <div style="height: 100%;width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-size: 22px;"><strong>                       <span style="text-decoration: underline;">UAC </span></strong><span style="text-decoration: underline;"><strong>- YOUR BILL.</strong></span></h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 22px;">Name: {NAME}</h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 22px;">Address: {ADDRESS}</h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 22px;">Weight: {WEIGHT}</h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 22px;">Contact: {CONTACT}</h1>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="images/image-1.jpeg" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 480px;" width="480"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <h1 style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 22px;">Have A Safe Trip!</h1>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>


    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>

</body>

</html>
"""


def context_data():
    context = {
        'page_name' : '',
        'page_title' : '',
        'system_name' : 'Spaceship Bookings Managment System',
        'topbar' : True,
        'footer' : True,
    }
    return context


def reserve_form(request, pk=None):
    context = context_data()
    context['page'] = 'Search Result'
    if pk is None:
        messages.error(request, "Invalid Flight ID")
        
        return redirect('public-page')
    else:
        context['flight'] = models.Shuttles.objects.get(id=pk)
        return render(request, 'reservation.html', context)


def ticket(request):
  return render(request, 'tickets.html')

def home(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'home.html',context)
@csrf_exempt

def about(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('/success')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'about.html', context)

def more(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'more.html', context)

def xwing(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'xwing.html',context)

def ships(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'ships.html',context)

def goods(request):
    return render(request, 'goods.html')
    
def result(request, fromA=None, toA=None, departure = None):
    context = context_data()
    context['page'] = 'Search Result'
    if fromA is None and toA is None and departure is None:
        messages.error(request, "Invalid Search Inputs")
        return redirect('public-page')
    else:
        departure = datetime.datetime.strptime(departure, "%Y-%m-%d")
        year = departure.strftime("%Y")
        month = departure.strftime("%m")
        day = departure.strftime("%d")
        context['Shuttles'] = models.Shuttles.objects.filter(delete_flag=0,
                        departure__year = year,
                        departure__month = month,
                        departure__day = day,
                        ).order_by('departure').all()
    return render(request, 'result1.html',context)

def reserve(request,pk = None):
    context = context_data()
    context['page'] = 'Search Result'
    if pk is None:
        messages.error(request, "Invalid Flight ID")
        return redirect('public-page')
    elif request.method == 'POST':
        order_currency = 'INR'
        amount = 20000  
        client = razorpay.Client(auth =("rzp_test_EdU5TSF0kd7e8j","OEI298z6aU33vEHl6dMJ5o1p") )
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    else:
        context['flight'] = models.Shuttles.objects.get(id=pk)


        return render(request, 'reserve.html', context)



def success(request):
    return render(request,'success.html')

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        order_currency = 'INR'
        amount = 20000  
        client = razorpay.Client(auth =("rzp_test_EdU5TSF0kd7e8j","OEI298z6aU33vEHl6dMJ5o1p") )   
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,'payment_success.html')

def select(request):
    context = context_data()
    context['page'] = 'Search Available Flight'
    Spaceship = models.Spaceship.objects.filter(delete_flag = 0, status = 1).all()
    Spaceports = models.Spaceport.objects.filter(delete_flag = 0, status = 1).all()
    context['Spaceship'] = Spaceship
    context['Spaceports'] = Spaceports
    return render(request,'select.html',context)

@csrf_exempt

def transport(request,pk = None):
    if request.method == 'POST':
        form2 = forms.SaveTransport(request.POST)
        if form2.is_valid():
          email = form2.cleaned_data['email']
          name = form2.cleaned_data['first_name'] + " " + form2.cleaned_data['last_name']
          contact = form2.cleaned_data['contact']
          address = form2.cleaned_data['address']
          if not isinstance(email, list):
              email = [email]
          form2.save()
          weight = form2.cleaned_data['weight']
          mail1 = second_mailer.format(NAME=name, ADDRESS=address, WEIGHT=weight, CONTACT=contact)
          send_mail('Your Billing', "BILL", EMAIL_HOST_USER, email, html_message=mail1)
          form2.save()
          return redirect('payment_success')
        else:
            return HttpResponse("ERROR Resubmit Form Again!")
        context = {
        'form':form2,
        }    
    return render(request,'transport.html')

def save_Bookings(request,pk = None):
    resp = { 'status': 'failed', 'msg':'' }
    if not request.method == 'POST':
        resp['msg'] = "No data has been sent."
    else:
        form = forms.SaveBookings(request.POST)
        if form.is_valid():
          fid = str(form.cleaned_data['flight'])
          email = form.cleaned_data['email']
          name = form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name']
          gender = form.cleaned_data['gender']
          contact = form.cleaned_data['contact']
          
          number_of_slots_e = esfn[0]
          number_of_slots_f= fsfn[0]
          print(f"{number_of_slots_f} is the number of slots for first class!")
          print(f"{number_of_slots_e} is the number of slots for economy!")
          if not isinstance(email, list):
              email = [email]

          eorb = int(form.cleaned_data['type'])

          if number_of_slots_f <= 0 and eorb == 1:
            resp['msg'] = "There are no first class seats available at the moment."
            print('There are no seats available in first class at the moment.')
          elif number_of_slots_e <= 0 and eorb == 2:
            resp['msg'] = "There are no economy class seats available at the moment."

          else:
            real_fid = fid.split('[')[0]
            from_ = fid.split('[')[1].split('-')[0]
            to_ = fid.split('[')[1].split('-')[1].split(']')[0] 
            mail = html_mailer.format(NAME=name, FROM=from_, TO=to_, CONTACT=contact, FID=real_fid)
            send_mail('Your Booking Details', "Booking", EMAIL_HOST_USER, email, html_message=mail)
            form.save()
            client = razorpay.Client(auth =("rzp_test_EdU5TSF0kd7e8j","OEI298z6aU33vEHl6dMJ5o1p"))
            currency = 'INR'
            amount = 20000 
            payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
            resp['status'] = 'success'
            resp['msg'] = "Your Bookings has been sent. Our staff will reach as soon we sees your Bookings. Thank you!"
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str("<br />")
    return HttpResponse(json.dumps(resp), content_type="application/json")


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)