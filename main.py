import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("Data.csv", index_col="date")

bcr.bar_chart_race(

    df=df,

    filename="Azab.mp4",

    img_label_folder="bar_image_labels",

    fig_kwargs=
        {
            #'figsize': (26, 15),
            'figsize': (20, 11),
            'dpi': 120,
            'facecolor': '#F8FAFF'
        },
    fixed_max=True,
    steps_per_period=45,
    period_length=1000,

    colors=['#14213d','#9b2226'],

    title={
            'label': 'who has scored more goals?',
            'size': 28,
            'color': '#000000',
            'weight': 'bold',
            'pad': 12
        },
    period_label={
            'x': .95,
            'y': .15,
            'ha': 'right',
            'va': 'center',
            'size': 28,
            'weight':'bold',
        },
    # style the bar label text
    bar_label_font={'size': 18, 'weight': 'bold',},

    # style the labels in x and y axis
    tick_label_font={'size': 18, 'weight': 'bold',},

    bar_kwargs={'alpha': .99, 'lw': 0},

    period_template='{x:.0f}',

    bar_size=.4,

)