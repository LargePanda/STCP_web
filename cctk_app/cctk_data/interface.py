import os
print os.getcwd()
import cctk_query
data = cctk_query.index_cchar_rule("./cctk_app/cctk_data/dictionary/readable_multi.txt", "./cctk_app/cctk_data/dictionary/readable_multi_phrase")
print data
print "[INFO] LOADING DATA"

def get_info(schar):
	if schar not in data:
		return {'candidate': [schar], 'example': "", 'explain':""}
	else:
		return data[schar]
