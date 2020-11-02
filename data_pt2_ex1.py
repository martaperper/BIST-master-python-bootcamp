density = np.repeat([6,12,24],6)
season = np.repeat(['Spring','Summer']*3,3)
egg = np.array(
    [1.167,0.5,1.667,4,3.83,3.83,
     1.5,0.833,1,3.33,2.58,2.75,
     0.667,0.667,0.75,2.54,1.83,1.63],
    dtype=float
              )

data_ex1 = pd.DataFrame(
    list(zip(density, season,egg)), 
    columns =['Density', 'Season', 'Egg']
)

data_ex1