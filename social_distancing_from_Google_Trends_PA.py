import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def initializeSubPlot(axes,title,x_label = 'Dates' ,y_label = 'Change w.r.t. baseline',lockdownFlag = False):
	if lockdownFlag:
		axes.axvspan(pd.to_datetime('2020-03-16'), pd.to_datetime("today"), facecolor='g', alpha=0.5,label = "Lockdown Starts in the US")
	axes.axhline(linewidth=4, color='r',label = 'BaseLine')
	axes.set_title(title)
	axes.set_xlabel(x_label)
	axes.set_ylabel(y_label)
	axes.legend()
	axes.grid(True)

data = pd.read_csv("~/Downloads/Global_Mobility_Report.csv",parse_dates=['date'])
data_pa = data[data.sub_region_1 == 'Pennsylvania']
data['avg_soc_dist'] = data_pa[['retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']].mean(axis=1)
data_pa['avg_soc_dist'] = data_pa[['retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']].fillna(0).mean(axis=1)
# x = np.array(data_pa.date.index.values)
y_max=data_pa.date.max()
y_min=data_pa.date.min()
howfar=7
first_day=y_min
dates = pd.date_range(f"{first_day}", periods=howfar, freq="d")

x_global = np.array(data.date.index.values)
plt.plot_date(data_pa['date'], y_data, 'g-', label = 'Global Trends')
plt.plot_date(data_pa['date'],data_pa['avg_soc_dist'],'b:', label = 'PA Trends')
plt.plot_date(data_pa['date'], np.zeros(data_pa.shape[0]),'r--', label = 'BaseLine')

# plt.plot(x,data_pa['avg_soc_dist'],'b:', label = 'PA Trends')
# plt.plot(x, np.zeros(data_pa.shape[0]), 'r--', label = 'BaseLine')
y_global_mean = data[['retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']].fillna(0).mean(axis=1)
# x_global = np.array(data.date.index.values)
mask = (data.date>=y_min) & (data.date<=y_max) & (~data.avg_soc_dist.isna())
y_data = data.avg_soc_dist[mask]
#Selected counties
selected_PA = ['Bradford County','Lackawanna County','Susquehanna County','Wayne County','Wyoming County']
# data_pa[data_pa.sub_region_1.isin(selected_PA)]
data_pa_counties = data_pa[data_pa.sub_region_2.isin(selected_PA)]
# plt.plot(x, y_data, 'g--', label = 'Global Trends')
fig, ax = plt.subplots(figsize=(16, 10), ncols=2, nrows=2, sharex=True)
axx=ax[0,0]
title = "Global Trends"
axx.plot_date(data['date'],data.avg_soc_dist,label = title )
initializeSubPlot(axx,title)
# axx.plot_date(data_pa['date'], np.zeros(data_pa.shape[0]),'r--', label = 'BaseLine')
# axx.set_title("Global Trends")
# axx.set_xlabel(x_label)
# axx.set_ylabel()
# axx.legend()
# axx.grid(True)
axx=ax[0,1]
title = "US Trends"
# yy=np.linspace(-y_data.max(),y_data.max())
# a = [pd.to_datetime('2020-03-16') for i in range(1,len(yy)+1)]
# dd = pd.DataFrame(a,columns=['date'])
# axx.plot_date(data_pa['date'], np.zeros(data_pa.shape[0]),'r--', label = 'BaseLine')
# axx.plot_date(dd,yy,'r-x',label = 'Lockdown implemented in the US')
# axx=ax[1]
axx.plot_date(data_pa['date'], y_data, 'g-', label = title)
initializeSubPlot(axx,title,lockdownFlag = True)
# axx.set_title('US Trends')
# axx.set_xlabel('Dates')
# axx.set_ylabel('Change w.r.t. baseline')
# axx.legend()
# axx.grid(True)
axx=ax[1,0]
title = "PA Trends"
# x_label = 'Dates'
# y_label = 'Change w.r.t. baseline'
axx.plot_date(data_pa['date'],data_pa['avg_soc_dist'],'b--', label = title)
initializeSubPlot(axx,title,lockdownFlag = True)
# axx.plot_date(data_pa['date'], np.zeros(data_pa.shape[0]),'r--', label = 'BaseLine')
# # axx.set_title('PA Trends')
# axx.set_xlabel('Dates')
# axx.set_ylabel('Change w.r.t. baseline')
# axx.legend()
# axx.grid(True)
axx=ax[1,1]
title = "GCMC Counties"

for i in range(0,len(selected_PA)):
	data_c = data_pa_counties[data_pa_counties.sub_region_2 == selected_PA[i]]
	axx.plot_date(data_c['date'],data_c.avg_soc_dist,label = selected_PA[i])
initializeSubPlot(axx,title,lockdownFlag = True)

# axx.plot_date(data_pa_counties['date'],data_pa_counties.avg_soc_dist == selected_PA[1],label = "Lackawanna")
# axx.plot_date(data_pa_counties['date'],data_pa_counties.avg_soc_dist == selected_PA[2],label = "Susquehanna")
# axx.plot_date(data_pa_counties['date'],data_pa_counties.avg_soc_dist == selected_PA[3],label = "Wayne")
# axx.plot_date(data_pa_counties['date'],data_pa_counties.avg_soc_dist == selected_PA[4],label = "Wyoming")
# axx.set_title("GCMC Counties")
# axx.set_xlabel('Dates')
# axx.set_ylabel('Change w.r.t. baseline')
# axx.legend()
# axx.grid(True)



fig.autofmt_xdate()
fig.tight_layout()

fig,ax = createSubPlot()
# fig.set_title("Change in Social Distancing Measures Trends")
# plt.legend()

def createSubPlot():
	fig, ax = plt.subplots(figsize=(16, 10), ncols=2, nrows=2, sharex=True)
	axx=ax[0,0]
	title = "Global Trends"
	axx.plot_date(data['date'],data.avg_soc_dist,label = title )
	initializeSubPlot(axx,title)
	axx=ax[0,1]
	title = "US Trends"
	axx.plot_date(data_pa['date'], y_data, 'g-', label = title)
	initializeSubPlot(axx,title,lockdownFlag = True)
	axx=ax[1,0]
	title = "PA Trends"
	axx.plot_date(data_pa['date'],data_pa['avg_soc_dist'],'b--', label = title)
	initializeSubPlot(axx,title,lockdownFlag = True)
	axx=ax[1,1]
	title = "GCMC Counties"
	for i in range(0,len(selected_PA)):
		data_c = data_pa_counties[data_pa_counties.sub_region_2 == selected_PA[i]]
		axx.plot_date(data_c['date'],data_c.avg_soc_dist,label = selected_PA[i])
	initializeSubPlot(axx,title,lockdownFlag = True)
	fig.autofmt_xdate()
	fig.tight_layout()
	return fig,ax