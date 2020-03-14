import crawling as cr
import step as st

# 최근 추점정보
drw_dict = cr.get_current_drw()

# 최근 추첨정보의 step 값
drw_list = st.step_by_one(drw_dict['drw_numbers'])

print(drw_list)