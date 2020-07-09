#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initial
total_cost = 500000  # Dream home - Căn nhà mơ ước :))
annual_salary = 120000.0 # Đồng lương chết đói mỗi năm
portion_saved = .05  # Phần tiền dành ra mỗi tháng sau khi nhận lương để mua nhà
semi_annual_raise = .03 # Hệ số tăng lương


# In[2]:


portion_down_payment = 0.25*total_cost # Số tiền đặt cọc
r = 0.04 # Lãi suất hàng năm


# In[3]:


def calculate_months():
    current_savings = 0.0 # Số tiền dành dụm :v
    month_salary = annual_salary/12
    
    for i in range(1, 1000):
        current_savings += month_salary*portion_saved + current_savings*r/12
        
        if i%6 == 0:
            month_salary += month_salary*semi_annual_raise
        
        if portion_down_payment < current_savings:
            return i


# In[4]:


print(calculate_months())

