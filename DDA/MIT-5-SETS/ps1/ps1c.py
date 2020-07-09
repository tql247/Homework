#!/usr/bin/env python
# coding: utf-8

# In[29]:


semi_annual_raise = .07 # Hệ số tăng
r = 0.04 # Lãi suất hàng năm
total_cost = 1000000  # Dream home - Căn nhà mơ ước :))
portion_down_payment = 0.25*total_cost # Số tiền đặt cọc
step = 0 # Bisection search
annual_salary = 150000 # input here
min_portion = 0
max_portion = 10000 # between 0% and 100%


# In[30]:


while True:
    current_savings = 0
    portion_saved = (min_portion + max_portion)/2
    month_salary = annual_salary / 12
    
    for m in range(36):
        current_savings += month_salary*(portion_saved/10000) + current_savings*r/12
        
#         Increase salary each 6 months
        if m%6 == 0: 
            month_salary += month_salary*semi_annual_raise
        
#     When saved enough to down the payment
    if abs(current_savings - portion_down_payment) <= 100:
        print('Best saving rate: %.4f' % (portion_saved / 10000))
        print('Step in binary search: ' + str(step))
        break
          
#     portion saving too much
    elif abs(current_savings - portion_down_payment) > 100 and current_savings > portion_down_payment:
        max_portion = portion_saved
        
#     portion saving too less
    elif abs(current_savings - portion_down_payment) > 100 and current_savings < portion_down_payment:
        min_portion = portion_saved
        
    if min_portion == max_portion:
        print('Dream house so far!')
        break
    
    step += 1


# In[ ]:





# In[ ]:




