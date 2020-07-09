#!/usr/bin/env python
# coding: utf-8

# In[84]:


# Initial
total_cost = 500000  # Dream home - Căn nhà mơ ước :))
annual_salary = 80000.0 # Đồng lương chết đói mỗi năm
portion_saved = .15  # Tiền dành ra mỗi tháng sau khi nhận lương để mua nhà


# In[85]:


portion_down_payment = 0.25*total_cost # Số tiền đặt cọc
r = 0.04 # Lãi suất hàng năm


# In[86]:


def calculate_months():
    current_savings = 0.0 # Số tiền dành dụm :v
    month_salary = annual_salary/12
    
    for i in range(1000):
        
        if portion_down_payment < current_savings:
            return i
        
        current_savings += month_salary*portion_saved + current_savings*r/12


# In[87]:


print(calculate_months())

