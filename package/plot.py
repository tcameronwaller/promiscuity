"""
...

"""

###############################################################################
# Notes

###############################################################################
# Installation and importation

# Standard
import os
import pickle
import itertools
import statistics
import copy

# Relevant
import pandas
import numpy
import scipy
import matplotlib
matplotlib.use("agg")
matplotlib.rcParams.update({'figure.max_open_warning': 0})
import matplotlib.pyplot
import matplotlib.lines
#import matplotlib_venn
#import seaborn
#import sklearn

# Custom

#import assembly
#import selection
#import integration
#import prediction
import promiscuity.utility as utility

#dir()
#importlib.reload()

###############################################################################
# Functionality


def define_font_properties():
    """
    Defines font properties.

    arguments:

    raises:

    returns:
        (dict<object>): references to definitions of font properties

    """

    # Define font values.
    values_one = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 1000,
        "weight": 1000,
        "size": 30
    }
    values_two = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 900,
        "weight": 1000,
        "size": 25
    }
    values_three = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 750,
        "weight": 1000,
        "size": 20
    }
    values_four = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 500,
        "weight": 500,
        "size": 17
    }
    values_five = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 400,
        "weight": 400,
        "size": 15
    }
    values_six = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 300,
        "weight": 300,
        "size": 13
    }
    values_seven = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 300,
        "weight": 300,
        "size": 10
    }
    values_eight = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 200,
        "weight": 200,
        "size": 7
    }
    values_nine = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 150,
        "weight": 150,
        "size": 5
    }
    values_ten = {
        "family": "sans-serif",
        "style": "normal",
        "variant": "normal",
        "stretch": 100,
        "weight": 100,
        "size": 3
    }
    # Define font properties.
    properties_one = matplotlib.font_manager.FontProperties(
        family=values_one["family"],
        style=values_one["style"],
        variant=values_one["variant"],
        stretch=values_one["stretch"],
        weight=values_one["weight"],
        size=values_one["size"]
    )
    properties_two = matplotlib.font_manager.FontProperties(
        family=values_two["family"],
        style=values_two["style"],
        variant=values_two["variant"],
        stretch=values_two["stretch"],
        weight=values_two["weight"],
        size=values_two["size"]
    )
    properties_three = matplotlib.font_manager.FontProperties(
        family=values_three["family"],
        style=values_three["style"],
        variant=values_three["variant"],
        stretch=values_three["stretch"],
        weight=values_three["weight"],
        size=values_three["size"]
    )
    properties_four = matplotlib.font_manager.FontProperties(
        family=values_four["family"],
        style=values_four["style"],
        variant=values_four["variant"],
        stretch=values_four["stretch"],
        weight=values_four["weight"],
        size=values_four["size"]
    )
    properties_five = matplotlib.font_manager.FontProperties(
        family=values_five["family"],
        style=values_five["style"],
        variant=values_five["variant"],
        stretch=values_five["stretch"],
        weight=values_five["weight"],
        size=values_five["size"]
    )
    properties_six = matplotlib.font_manager.FontProperties(
        family=values_six["family"],
        style=values_six["style"],
        variant=values_six["variant"],
        stretch=values_six["stretch"],
        weight=values_six["weight"],
        size=values_six["size"]
    )
    properties_seven = matplotlib.font_manager.FontProperties(
        family=values_seven["family"],
        style=values_seven["style"],
        variant=values_seven["variant"],
        stretch=values_seven["stretch"],
        weight=values_seven["weight"],
        size=values_seven["size"]
    )
    properties_eight = matplotlib.font_manager.FontProperties(
        family=values_eight["family"],
        style=values_eight["style"],
        variant=values_eight["variant"],
        stretch=values_eight["stretch"],
        weight=values_eight["weight"],
        size=values_eight["size"]
    )
    properties_nine = matplotlib.font_manager.FontProperties(
        family=values_nine["family"],
        style=values_nine["style"],
        variant=values_nine["variant"],
        stretch=values_nine["stretch"],
        weight=values_nine["weight"],
        size=values_nine["size"]
    )
    properties_ten = matplotlib.font_manager.FontProperties(
        family=values_ten["family"],
        style=values_ten["style"],
        variant=values_ten["variant"],
        stretch=values_ten["stretch"],
        weight=values_ten["weight"],
        size=values_ten["size"]
    )
    # Compile and return references.
    return {
        "values": {
            "one": values_one,
            "two": values_two,
            "three": values_three,
            "four": values_four,
            "five": values_five,
            "six": values_six,
            "seven": values_seven,
            "eight": values_eight,
            "nine": values_nine,
            "ten": values_ten,
        },
        "properties": {
            "one": properties_one,
            "two": properties_two,
            "three": properties_three,
            "four": properties_four,
            "five": properties_five,
            "six": properties_six,
            "seven": properties_seven,
            "eight": properties_eight,
            "nine": properties_nine,
            "ten": properties_ten,
        }
    }


def define_color_properties():
    """
    Defines color properties.

    arguments:

    raises:

    returns:
        (dict<tuple>): references to definitions of color properties

    """

    # Black.
    black = (0.0, 0.0, 0.0, 1.0)
    # Gray.
    gray = (0.7, 0.7, 0.7, 1.0)
    # White.
    white = (1.0, 1.0, 1.0, 1.0)
    white_faint = (1.0, 1.0, 1.0, 0.75)
    # Clear.
    clear = (1.0, 1.0, 1.0, 0.0)
    clear_faint = (1.0, 1.0, 1.0, 0.25)
    # Blue.
    blue = (0.0, 0.2, 0.5, 1.0)
    blue_faint = (0.0, 0.2, 0.5, 0.75)
    # Orange.
    orange = (1.0, 0.6, 0.2, 1.0)
    orange_faint = (1.0, 0.6, 0.2, 0.75)
    # Compile and return references.
    return {
        "black": black,
        "gray": gray,
        "white": white,
        "white_faint": white_faint,
        "clear": clear,
        "clear_faint": clear_faint,
        "blue": blue,
        "blue_faint": blue_faint,
        "orange": orange,
        "orange_faint": orange_faint
    }


# TODO: pass variable for label on scale bar...

def plot_heatmap_symmetric_diverge(
    data=None,
    minimum=None,
    maximum=None,
    label_rows=None,
    label_columns=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type heatmap.

    arguments:
        data (object): Pandas data frame of quantitative values with mappings
            to columns and rows that will be transposed in heatmap
        minimum (float): minimal value
        maximum (float): maximal value
        label_rows (bool): whether to include explicit labels on heatmap's rows
        label_columns (bool): whether to include explicit labels on heatmap's
            columns
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    # Map data's columns to heatmap's rows.
    # Map data's rows to heatmap's columns.
    labels_rows = data.columns.to_list()
    labels_columns = data.index.to_list()
    matrix = numpy.transpose(data.to_numpy())

    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    axes = matplotlib.pyplot.axes()

    # Represent data as a color grid.
    image = axes.imshow(
        matrix,
        cmap="PuOr", # "PuOr", "RdBu" diverging color map
        vmin=minimum,
        vmax=maximum,
        aspect="equal",
        origin="upper",
        # Extent: (left, right, bottom, top)
        #extent=(-0.5, (matrix.shape[1] - 0.5), (matrix.shape[0] - 0.5), -0.5),
    )

    # Create legend for color map.
    label_bar = "Spearman correlation (FDR <= 0.05)"
    bar = axes.figure.colorbar(
        image,
        orientation="vertical",
        ax=axes,
    )
    bar.ax.set_ylabel(
        label_bar,
        rotation=-90,
        va="bottom",
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["three"],
    )
    bar.ax.tick_params(
        axis="both",
        which="both", # major, minor, or both
        direction="out",
        length=5.0,
        width=2.0,
        color=colors["black"],
        pad=2,
        labelsize=fonts["values"]["five"]["size"],
        labelcolor=colors["black"],
    )

    # Create ticks and labels for each grid.
    # Let the horizontal axes labeling appear on top.
    axes.tick_params(
        axis="both",
        which="both", # major, minor, or both
        direction="out",
        length=5.0,
        width=1.0,
        color=colors["black"],
        pad=5,
        labelcolor=colors["black"],
        top=True,
        bottom=False, # False
        left=True,
        right=False,
        labeltop=True,
        labelbottom=False,
        labelleft=True,
        labelright=False,
    )

    # Create ticks and labels.
    if (label_columns and data.shape[1] <= 100):
        if (100 >= data.shape[1] and data.shape[1] >= 90):
            size_column = "ten"
        elif (90 > data.shape[1] and data.shape[1] >= 75):
            size_column = "nine"
        elif (75 > data.shape[1] and data.shape[1] >= 50):
            size_column = "eight"
        elif (50 > data.shape[1] and data.shape[1] >= 25):
            size_column = "seven"
        elif (25 > data.shape[1]):
            size_column = "six"
        axes.set_xticks(numpy.arange(matrix.shape[1]))
        axes.set_xticklabels(
            labels_columns,
            #minor=False,
            rotation=-60,
            rotation_mode="anchor",
            ha="right", # horizontal alignment
            va="bottom", # vertical alignment
            alpha=1.0,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"][size_column]
        )
    if (label_rows and data.shape[0] <= 100):
        if (100 >= data.shape[0] and data.shape[0] >= 90):
            size_row = "nine"
        elif (90 > data.shape[0] and data.shape[0] >= 75):
            size_row = "eight"
        elif (75 > data.shape[0] and data.shape[0] >= 50):
            size_row = "six"
        elif (50 > data.shape[0] and data.shape[0] >= 25):
            size_row = "five"
        elif (25 > data.shape[0]):
            size_row = "three"
        axes.set_yticks(numpy.arange(matrix.shape[0]))
        axes.set_yticklabels(
            labels_rows,
            #minor=False,
            ha="right", # horizontal alignment
            va="center", # vertical alignment
            alpha=1.0,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"][size_row]
        )
    if False:
        # Rotate the tick labels and set their alignment.
        matplotlib.pyplot.setp(
            axes.get_xticklabels(),
            rotation=-30,
            ha="right",
            rotation_mode="anchor"
        )
        pass
    # Return figure.
    return figure


# TODO: accommodate different variable types... categorical, continuous divergent, continuous, ordinal, etc...


def organize_heatmap_asymmetric_data(
    data=None,
):
    """
    Organizes data for chart.

    arguments:
        data (object): Pandas data frame of quantitative values with mappings
            to columns and rows that will be transposed in heatmap

    raises:

    returns:
        (dict): collection of information for chart

    """

    # Copy data.
    data = data.copy(deep=True)
    # Map data's columns to heatmap's rows.
    # Map data's rows to heatmap's columns.
    labels_rows = data.columns.to_list()
    labels_columns = data.index.to_list()
    matrix = numpy.transpose(data.to_numpy())
    # Determine maximal and minimal values.
    array = matrix.flatten()
    minimum = round(numpy.nanmin(array), 2)
    maximum = round(numpy.nanmax(array), 2)
    # Collect information.
    bin = dict()
    bin["data"] = data
    bin["matrix"] = matrix
    bin["minimum"] = minimum
    bin["maximum"] = maximum
    bin["labels_rows"] = labels_rows
    bin["labels_columns"] = labels_columns
    # Return information.
    return bin


def plot_heatmap_asymmetric(
    data=None,
    title=None,
    label_scale=None,
    type=None,
    label_rows=None,
    label_columns=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type heatmap.

    arguments:
        data (object): Pandas data frame of quantitative values with mappings
            to columns and rows that will be transposed in heatmap
        title (str): title for top left of figure
        label_scale (str): label for heatmap scale bar
        type (str): type of property, category, binary, ordinal, continuous, or
            continuous_divergent
        label_rows (bool): whether to include explicit labels on heatmap's rows
        label_columns (bool): whether to include explicit labels on heatmap's
            columns
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    bucket = organize_heatmap_asymmetric_data(
        data=data,
    )
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811), # 40 cm, 30 cm
        tight_layout=True,
    )
    figure.suptitle(
        title,
        x=0.01,
        y=0.99,
        ha="left",
        va="top",
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"]
    )
    axes = matplotlib.pyplot.axes()
     # Main chart in bottom panel.
    organize_heatmap_asymmetric_master_main_bottom(
        label_scale=label_scale,
        type=type,
        matrix=bucket["matrix"],
        minimum=bucket["minimum"],
        maximum=bucket["maximum"],
        labels_rows=bucket["labels_rows"],
        labels_columns=bucket["labels_columns"],
        fonts=fonts,
        colors=colors,
        axis_main=axes,
        axis_scale=axes,
        figure=figure,
     )

    return figure


# Asymmetric heatmap with master and main panels
# Sort by master variable and cluster by similarities
# TODO: would this set of functions be more appropriate for the utility module?

def organize_data_master_main_sort_cluster(
    type_master=None,
    sequence=None,
    data=None,
    index=None,
):
    """
    Organize sort and cluster of data.

    arguments:
        type_master (str): type of master variable, category, binary, ordinal,
            or continuous
        data (object): Pandas data frame of main and master feature variables
            across instances
        index (str): name of index that is common between data_master and
            data_main
        sequence (str): method to determine sequence of instances, sort by
            master variable's values or cluster by similarities across features


    raises:

    returns:
        (object): Pandas data frame of pan-tissue signals across genes and
            persons with property

    """

    if (sequence == "sort"):
        data.sort_values(
            by=["master"],
            axis="index",
            ascending=True,
            inplace=True,
        )
        data_cluster_columns = utility.cluster_data_columns(
            data=data,
        )
        data_cluster_columns.reset_index(
            level=None,
            inplace=True
        )
        data_cluster_columns.set_index(
            [index],
            append=False,
            drop=True,
            inplace=True
        )
        if (type_master in ["category", "binary", "ordinal"]):
            data_cluster_columns.reset_index(
                level=None,
                inplace=True
            )
            data_cluster_columns.set_index(
                [index, "master"],
                append=False,
                drop=True,
                inplace=True
            )
            data_cluster_rows = utility.cluster_data_rows_by_group(
                group="master",
                index=index,
                data=data_cluster_columns,
            )
            # Organize data.
            data_cluster_rows.reset_index(
                level=None,
                inplace=True
            )
            data_cluster_rows.set_index(
                [index],
                append=False,
                drop=True,
                inplace=True
            )
            data_sequence = data_cluster_rows.copy(deep=True)
        else:
            data_sequence = data_cluster_columns.copy(deep=True)
    elif (sequence == "cluster"):
        data_cluster_columns = utility.cluster_data_columns(
            data=data,
        )
        data_cluster_rows = utility.cluster_data_rows(
            data=data_cluster_columns,
        )
        data_sequence = data_cluster_rows.copy(deep=True)
    # Return information.
    return data_sequence


def organize_data_master_main(
    data_master=None,
    master=None,
    type_master=None,
    data_main=None,
    type_main=None,
    scale_unit_main=None,
    columns_main_scale_unit=None,
    fill_missing=None,
    index=None,
    sequence=None,
):
    """
    Organize information to sort multiple main data variables by a single
    master variable.

    Data have features across columns and instances across rows.

    Sequence of features depends on hierarchical cluster by their
    similarities across instances.
    Sequence of instances depends either on sort by values of master variable
    or on hierarchical cluster by their similarities across features.

    arguments:
        data_master (object): Pandas data frame including master variable
            across instances that match those of data_main
        master (str): name of feature in data_master that is master variable
        type_master (str): type of master variable, category, binary, ordinal,
            or continuous
        data_main (object): Pandas data frame of feature variables across
            instances that match those of data_master
        type_main (str): type of main variables, category, binary, ordinal,
            continuous, or continuous_divergent
        scale_unit_main (bool): whether to scale columns in data_main
        columns_main_scale_unit (list<str>): names of columns in data_main to
            scale to unit distribution between 0 and 1
        fill_missing (bool): whether to fill missing values with zero
        index (str): name of index that is common between data_master and
            data_main
        sequence (str): method to determine sequence of instances, sort by
            master variable's values or cluster by similarities across features

    raises:

    returns:
        (dict): information for chart

    """

    # Copy data.
    data_master = data_master.copy(deep=True)
    data_main = data_main.copy(deep=True)

    # Organize main variables.
    # Drop any rows or columns in main data with only missing values.
    data_main.dropna(
        axis="index",
        how="all",
        inplace=True,
    )
    data_main.dropna(
        axis="columns",
        how="all",
        inplace=True,
    )
    # Scale main variable values.
    if scale_unit_main:
        data_main_scale = data_main.apply(
            lambda column:
                sklearn.preprocessing.minmax_scale(
                    column.to_numpy(),
                    feature_range=(0, 1),
                    axis=0,
                    copy=True,
                ) if (column.name in columns_main_scale_unit) else column,
            axis="index",
        )
    else:
        data_main_scale = data_main
    # Replace missing values in main data with zero.
    if fill_missing:
        # Set any infinite values to missing.
        data_main_scale[data_main_scale == numpy.inf] = numpy.nan
        data_main_scale.fillna(
            value=0.0,
            #axis="columns",
            inplace=True,
        )
    else:
        data_main_scale.fillna(
            value=-1.0,
            #axis="columns",
            inplace=True,
        )
    # Organize master variable.
    if (type_master in ["category", "binary", "ordinal"]):
        data_master["master"], labels_categories_master = pandas.factorize(
            data_master[master],
            sort=True
        )
        labels_categories_master = list(labels_categories_master)
    elif type_master == "continuous":
        data_master["master"] = data_master[master]
        labels_categories_master = list()
    data_master = data_master.loc[
        :, data_master.columns.isin(["master", master])
    ]
    # Join master and main data.
    data_hybrid = data_main_scale.join(
        data_master,
        how="left",
        on=index
    )
    data_hybrid.drop(
        labels=[master],
        axis="columns",
        inplace=True
    )
    # Drop any rows in hybrid data with missing values in master.
    data_hybrid.dropna(
        axis="index",
        how="all",
        subset=["master"],
        inplace=True,
    )
    # Sort and cluster data.
    if sequence != "none":
        data_hybrid_sequence = organize_data_master_main_sort_cluster(
            type_master=type_master,
            sequence=sequence,
            data=data_hybrid,
            index=index,
        )
    else:
        data_hybrid_sequence = data_hybrid
    # Compile information.
    bin = dict()
    bin["labels_categories_master"] = labels_categories_master
    bin["data"] = data_hybrid_sequence
    # Return information
    return bin


def organize_heatmap_asymmetric_master_main_data(
    data=None,
):
    """
    Organizes data for chart.

    arguments:
        data (object): Pandas data frame of quantitative values with mappings
            to columns and rows that will be transposed in heatmap

    raises:

    returns:
        (dict): collection of information for chart

    """

    # Copy data.
    data_master = data.copy(deep=True)
    data_main = data.copy(deep=True)
    # Groups.
    values_master = data_master["master"].to_list()
    values_master_unique = utility.collect_unique_elements(
        elements_original=values_master,
    )
    # Map data's columns to heatmap's rows.
    # Map data's rows to heatmap's columns.
    data_main.drop(
        labels=["master"],
        axis="columns",
        inplace=True
    )
    labels_rows_main = data_main.columns.to_list()
    labels_columns_main = data_main.index.to_list()
    matrix_main = numpy.transpose(data_main.to_numpy())
    # Determine maximal and minimal values.
    minimum_master = round(min(values_master), 2)
    maximum_master = round(max(values_master), 2)
    array_main = matrix_main.flatten()
    minimum_main = round(numpy.nanmin(array_main), 2)
    maximum_main = round(numpy.nanmax(array_main), 2)

    # Collect information.
    bin = dict()
    bin["data_master"] = data_master
    bin["values_master"] = values_master
    bin["values_master_unique"] = values_master_unique
    bin["minimum_master"] = minimum_master
    bin["maximum_master"] = maximum_master
    bin["data_main"] = data_main
    bin["matrix_main"] = matrix_main
    bin["minimum_main"] = minimum_main
    bin["maximum_main"] = maximum_main
    bin["labels_rows_main"] = labels_rows_main
    bin["labels_columns_main"] = labels_columns_main
    # Return information.
    return bin


def initialize_heatmap_asymmetric_master_main_figure_axes(
    title=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type heatmap.

    arguments:
        title (str): title for chart
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object, object): instances of figure and axes objects

    """

    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811), # 40 cm, 30 cm
        #tight_layout=True,
    )
    figure.suptitle(
        title,
        x=0.01,
        y=0.99,
        ha="left",
        va="top",
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"]
    )
    axes = figure.subplots(
        nrows=2,
        ncols=2,
        sharex=False,
        sharey=False,
        #squeeze=True,
        gridspec_kw=dict(
            hspace=0.05,
            wspace=0.05,
            height_ratios=[1, 10],
            width_ratios=[50, 1],
            left=0.11,
            right=0.94,
            top=0.94,
            bottom=0.05,
        ),
    )
    # Return information.
    return figure, axes


def organize_heatmap_asymmetric_master_main_top(
    title_subordinate=None,
    label=None,
    type=None,
    values=None,
    values_unique=None,
    labels_categories=None,
    minimum=None,
    maximum=None,
    fonts=None,
    colors=None,
    axes=None,
    figure=None,
):
    """
    Organizes top panel of figure.

    arguments:
        title_subordinate (str): subordinate title for top right of figure
        label (str): label for master heatmap
        type (str): type of property, category or continuity
        values (list): values of property
        values_unique (list): unique values of property
        labels_categories (list<str>): labels for categorical ticks
        minimum (float): minimal value of property
        maximum (float): maximal value of property
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        axes (object): instance axis object
        figure (object): instance figure object

    raises:

    returns:
        (object): figure object

    """

    # Define color map and labels.
    if ((type == "category") or (type == "binary") or (type == "ordinal")):
        #color_map = matplotlib.colors.ListedColormap(
        #    [colors["blue"], colors["orange"]], 2
        #)
        color_map = matplotlib.pyplot.get_cmap("GnBu", len(values_unique))
        ticks = values_unique
        labels_ticks = labels_categories
    elif (type == "continuous"):
        color_map = "GnBu"
        ticks = [minimum, maximum]
        labels_ticks = [minimum, maximum]
    # Initialize chart.
    image = axes[0, 0].imshow(
        [values],
        cmap=color_map,
        vmin=minimum,
        vmax=maximum,
        aspect="auto",
        origin="upper",
        # Extent: (left, right, bottom, top)
        extent=(-0.5, (len(values) - 0.5), (1 + 0.5), -0.5),
    )
    axes[0, 0].set_yticks(numpy.arange(1))
    axes[0, 0].set_yticklabels(
        [str(label)],
        #minor=False,
        ha="right", # horizontal alignment
        va="center", # vertical alignment
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["four"]
    )
    axes[0, 0].set_xlabel(
        str(title_subordinate),
        rotation=0,
        ha="right",
        va="bottom",
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["three"],
    )
    #bar_group.ax.xaxis.set_label_position("top")
    axes[0, 0].xaxis.set_label_coords(1.0, 1.2)
    axes[0, 0].tick_params(
        axis="both",
        which="both", # major, minor, or both
        direction="out",
        length=5.0,
        width=3.0,
        pad=7,
        top=False,
        bottom=False,
        left=True,
        right=False,
        labeltop=False,
        labelbottom=False,
        labelleft=True,
        labelright=False,
        #color=colors["black"],
        #labelsize=fonts["values"]["four"]["size"],
        #labelcolor=colors["black"],
    )
    # Create legend for color map.
    bar = figure.colorbar(
        image,
        cax=axes[0, 1],
        ticks=ticks,
        orientation="vertical",
        use_gridspec=True,
    )
    bar.ax.set_yticklabels(
        labels_ticks,
        #minor=False,
        ha="left", # horizontal alignment
        va="bottom", # vertical alignment
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["four"]
    )
    bar.ax.tick_params(
        axis="both",
        which="both", # major, minor, or both
        direction="out",
        length=5.0,
        width=3.0,
        pad=7,
        top=False,
        bottom=False,
        left=False,
        right=True,
        labeltop=False,
        labelbottom=False,
        labelleft=False,
        labelright=True,
        #color=colors["black"],
        #labelsize=fonts["values"]["four"]["size"],
        #labelcolor=colors["black"],
    )
    pass


def organize_heatmap_asymmetric_master_main_bottom(
    label_scale=None,
    type=None,
    matrix=None,
    minimum=None,
    maximum=None,
    labels_rows=None,
    labels_columns=None,
    fonts=None,
    colors=None,
    axis_main=None,
    axis_scale=None,
    figure=None,
):
    """
    Organizes top panel of figure.

    arguments:
        label_scale (str): label for heatmap scale bar
        type (str): type of property, category, binary, ordinal, continuous, or
            continuous_divergent
        matrix (array<array>): values of properties
        minimum (float): minimal value of property
        maximum (float): maximal value of property
        labels_rows (list<str>): labels for matrix rows
        labels_columns (list<str>): labels for matrix columns
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        axis_main (object): instance of axis for main plot
        axis_scale (object): instance of axis for scale bar plot
        figure (object): instance figure object

    raises:

    returns:
        (object): figure object

    """

    # Define color map and labels.
    if (
        (type == "category") or
        (type == "binary") or
        (type == "ordinal") or
        (type == "continuous")
    ):
        color_map = "RdPu"
        scale = matplotlib.colors.Normalize(
            vmin=minimum,
            vmax=maximum,
        )
        ticks = [minimum, maximum]
        labels_ticks = [minimum, maximum]
    elif (type == "continuous_divergent"):
        color_map = "PuOr"
        scale = matplotlib.colors.TwoSlopeNorm(
            vmin=minimum,
            vcenter=0.0,
            vmax=maximum,
        )
        ticks = [minimum, 0.0, maximum]
        labels_ticks = [minimum, 0.0, maximum]

    # Initialize chart.
    image = axis_main.imshow(
        matrix,
        cmap=color_map, # sequential: "RdPu", diverging: "PuOr"
        aspect="auto", # "auto", "equal"
        origin="upper", # "lower" or "upper"
        # Extent: (left, right, bottom, top)
        #extent=(-0.5, (matrix.shape[1] - 0.5), (matrix.shape[0] - 0.5), -0.5),
        alpha=1.0,
        norm=scale,
        filternorm=True,
        resample=True,
    )
    #axes[2, 0].set_xlim(-10, (matrix.shape[1] + 10))
    #axes[2, 0].set_ylim(-3, (matrix.shape[0] + 3))

    # Create ticks and labels for each grid.
    # Let the horizontal axes labeling appear on top.
    if matrix.shape[0] <= 100:
        if (100 >= matrix.shape[0] and matrix.shape[0] >= 90):
            size_count = "ten"
        elif (90 > matrix.shape[0] and matrix.shape[0] >= 75):
            size_count = "nine"
        elif (75 > matrix.shape[0] and matrix.shape[0] >= 50):
            size_count = "eight"
        elif (50 > matrix.shape[0] and matrix.shape[0] >= 25):
            size_count = "seven"
        elif (25 > matrix.shape[0]):
            size_count = "three"
        axis_main.tick_params(
            axis="both",
            which="both",
            direction="out",
            length=5.0,
            width=3.0,
            pad=7,
            top=False,
            bottom=True,
            left=True,
            right=False,
            labeltop=False,
            labelbottom=True,
            labelleft=True,
            labelright=False,
            color=colors["black"],
            labelsize=fonts["values"][size_count]["size"],
            labelcolor=colors["black"],
        )
        axis_main.set_yticks(numpy.arange(matrix.shape[0]))
        axis_main.set_yticklabels(
            labels_rows,
            #minor=False,
            ha="right", # horizontal alignment
            va="center", # vertical alignment
            alpha=1.0,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"][size_count]
        )
        pass
    # Create legend for color map.
    if axis_scale is axis_main:
        bar = axis_main.figure.colorbar(
            image,
            orientation="vertical",
            ax=axis_main,
            ticks=ticks,
        )
    else:
        bar = figure.colorbar(
            image,
            cax=axis_scale,
            ticks=ticks,
            orientation="vertical",
            use_gridspec=True,
        )
        pass
    bar.ax.set_ylabel(
        label_scale,
        rotation=-90,
        ha="center",
        va="bottom",
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["three"],
    )
    bar.ax.yaxis.set_label_coords(2.5, 0.5)
    bar.ax.set_yticklabels(
        labels_ticks,
        #minor=False,
        ha="left", # horizontal alignment
        va="center", # vertical alignment
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["four"]
    )
    bar.ax.tick_params(
        axis="both",
        which="both", # major, minor, or both
        direction="out",
        length=5.0,
        width=3.0,
        pad=7,
        top=False,
        bottom=False,
        left=False,
        right=True,
        labeltop=False,
        labelbottom=False,
        labelleft=False,
        labelright=True,
        #color=colors["black"],
        #labelsize=fonts["values"]["four"]["size"],
        #labelcolor=colors["black"],
    )
    pass


def plot_heatmap_asymmetric_master_main_top_bottom(
    title=None,
    title_subordinate=None,
    label_master=None,
    labels_categories_master=None,
    label_main=None,
    type_master=None,
    type_main=None,
    data=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type heatmap.

    Data must have observations across rows.
    Data's observations must already be in sort order.
    Data must have features across columns.
    Data must also have a single column of name "master".
    Values in column "master" must be integers.

    The chart will organize features across rows and observations across
    columns.
    The chart will represent integer values of the group of each observation in
    a separate chart across columns.


    arguments:
        title (str): title for top left of figure
        title_subordinate (str): subordinate title for top right of figure
        label_master (str): label for left of master heatmap row
        labels_categories_master (list<str>): labels for scale ticks of
            categorical master variable
        label_main (str): label for main heatmap scale
        type_master (str): type of master variable, category, binary, ordinal,
            or continuous
        type_main (str): type of main variables, category, binary, ordinal,
            continuous, or continuous_divergent
        data (object): Pandas data frame of quantitative values with mappings
            to columns and rows that will be transposed in heatmap
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    bin_data = organize_heatmap_asymmetric_master_main_data(
        data=data,
    )
    # Initialize figure.
    figure, axes = initialize_heatmap_asymmetric_master_main_figure_axes(
        title=title,
        fonts=fonts,
        colors=colors,
    )

    # Master chart in top panel.
    organize_heatmap_asymmetric_master_main_top(
        title_subordinate=title_subordinate,
        label=label_master,
        type=type_master,
        values=bin_data["values_master"],
        values_unique=bin_data["values_master_unique"],
        labels_categories=labels_categories_master,
        minimum=bin_data["minimum_master"],
        maximum=bin_data["maximum_master"],
        fonts=fonts,
        colors=colors,
        axes=axes,
        figure=figure,
     )

     # Main chart in bottom panel.
    organize_heatmap_asymmetric_master_main_bottom(
        label_scale=label_main,
        type=type_main,
        matrix=bin_data["matrix_main"],
        minimum=bin_data["minimum_main"],
        maximum=bin_data["maximum_main"],
        labels_rows=bin_data["labels_rows_main"],
        labels_columns=bin_data["labels_columns_main"],
        fonts=fonts,
        colors=colors,
        axis_main=axes[1, 0],
        axis_scale=axes[1, 1],
        figure=figure,
     )

    # Return figure.
    return figure


def plot_distribution_histogram(
    array=None,
    title=None,
    bin_method=None,
    bin_count=None,
    label_bins=None,
    label_counts=None,
    fonts=None,
    colors=None,
    line=None,
    line_position=None,
    label_text=None,
    label_report=None,
):
    """
    Creates a figure of a chart of type histogram to represent the frequency
    distribution of a single series of values.

    Consider utility of numpy.digitize(), numpy.bincount(), numpy.unique(),
    and numpy.histogram().

    arguments:
        array (object): NumPy array of values
        title (str): title for figure
        bin_method (str): method to define bins, "count" or "auto"
        bin_count (int): count of bins to define and populate
        label_bins (str): label for bins
        label_counts (str): label for counts
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        line (bool): whether to draw a vertical line
        line_position (float): position for vertical line
        label_text (str): text to include on figure
        label_report (bool): whether to include label for report of count and
            mean of values

    raises:

    returns:
        (object): figure object

    """

    # Determine count and mean of values in array.
    count_values = int(array.size)
    mean_values = round(numpy.nanmean(array), 3)
    median_values = round(numpy.nanmedian(array), 3)
    # Define and populate bins.
    # Bin method "auto" is useful.
    #values, edges = numpy.histogram(series, bins=count_bins)
    if bin_method == "count":
        bin_edges = numpy.histogram_bin_edges(array, bins=bin_count)
    else:
        bin_edges = numpy.histogram_bin_edges(array, bins=bin_method)

    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    axes = matplotlib.pyplot.axes()
    values, bins, patches = axes.hist(
        array,
        bins=bin_edges,
        histtype="bar",
        align="left",
        orientation="vertical",
        rwidth=0.35,
        log=False,
        color=colors["blue"],
        label=title,
        stacked=False
    )
    if False:
        axes.set_title(
            title,
            #fontdict=fonts["properties"]["one"],
            loc="center",
        )
        axes.legend(
            loc="upper right",
            markerscale=2.5,
            markerfirst=True,
            prop=fonts["properties"]["one"],
            edgecolor=colors["black"]
        )
    axes.set_xlabel(
        xlabel=label_bins,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.set_ylabel(
        ylabel=label_counts,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"]
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["two"]["size"],
        labelcolor=colors["black"]
    )
    if line:
        axes.axvline(
            x=line_position,
            ymin=0,
            ymax=1,
            alpha=1.0,
            color=colors["orange"],
            linestyle="--",
            linewidth=7.5, # 3.0, 7.5
        )
    if len(label_text) > 0:
        matplotlib.pyplot.text(
            0.99,
            0.99,
            label_text,
            horizontalalignment="right",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white_faint"],
            color=colors["black"],
            fontproperties=fonts["properties"]["one"]
        )
    if label_report:
        matplotlib.pyplot.text(
            0.99,
            0.90,
            str("(count: " + str(count_values) + ")"),
            horizontalalignment="right",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white_faint"],
            color=colors["black"],
            fontproperties=fonts["properties"]["two"]
        )
        matplotlib.pyplot.text(
            0.99,
            0.85,
            str("(mean: " + str(mean_values) + ")"),
            horizontalalignment="right",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white_faint"],
            color=colors["black"],
            fontproperties=fonts["properties"]["two"]
        )
        matplotlib.pyplot.text(
            0.99,
            0.80,
            str("(median: " + str(median_values) + ")"),
            horizontalalignment="right",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white_faint"],
            color=colors["black"],
            fontproperties=fonts["properties"]["two"]
        )
    return figure


def plot_bar_stack(
    data=None,
    label_vertical=None,
    label_horizontal=None,
    fonts=None,
    colors=None,
    color_count=None,
    rotation=None,
    legend=None,
):
    """
    Creates a figure of a chart of type histogram to represent the frequency
    distribution of a single series of values.

    arguments:
        data (object): Pandas data frame of groups, series, and values
        label_vertical (str): label for vertical axis
        label_horizontal (str): label for horizontal axis
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        color_count (int): count of colors for subcategories (stacks)
        rotation (str): value for rotation of labels
        legend (bool): whether to include a legend for series on the chart

    raises:

    returns:
        (object): figure object

    """

    # Define groups and series.
    groups = list(data.loc[:, "groups"])
    data.set_index(
        ["groups"],
        append=False,
        drop=True,
        inplace=True
    )
    series_names = list(data.columns)

    if color_count == 1:
        colors_series = [colors["blue"]]
    elif color_count == 2:
        colors_series = [colors["blue"], colors["orange"]]
    elif color_count > 2:
        colors_series = list(
            seaborn.color_palette("hls", n_colors=color_count)
        )
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    # Create axes.
    axes = matplotlib.pyplot.axes()

    # Initialize bases.
    bases = list(itertools.repeat(0, len(groups)))
    # Initialize bars.
    bars = []
    # Iterate on series.
    index = 0
    for series_name in series_names:
        # Access series values.
        values = list(data.loc[:, series_name])
        print(series_name)
        print(values)
        # Create charts on axes.
        series_bars = axes.bar(
            range(len(groups)),
            values,
            width=0.8,
            bottom=bases,
            align="center",
            color=colors_series[index],
        )
        bars.append(series_bars[0])
        # Restore bases.
        bases = list(map(sum, zip(bases, values)))
        print(bases)
        index += 1
        pass

    axes.set_ylabel(
        ylabel=label_vertical,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"]
    )
    axes.set_xlabel(
        xlabel=label_horizontal,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"],
        rotation="horizontal",
    )
    axes.set_xticks(range(len(groups)), minor=False)
    axes.set_xticklabels(
        groups,
        rotation=-30,
        rotation_mode="anchor",
        ha="left", # horizontal alignment
        va="top", # vertical alignment
        minor=False,
        #rotation=rotation,
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["two"]["size"],
        labelcolor=colors["black"]
    )
    if legend:
        axes.legend(
            bars,
            series_names,
            loc="upper left",
            markerscale=2.5,
            markerfirst=True,
            prop=fonts["properties"]["one"],
            edgecolor=colors["black"]
        )
    return figure


def plot_boxes(
    arrays=None,
    labels_groups=None,
    label_vertical=None,
    label_horizontal=None,
    label_top_center=None,
    label_top_left=None,
    label_top_right=None,
    orientation=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type histogram to represent the frequency
    distribution of a single series of values.

    arguments:
        arrays (list<array>): NumPy arrays of values for each group
        labels_groups (list<str>): labels for each group
        label_vertical (str): label for vertical axis
        label_horizontal (str): label for horizontal axis
        label_top_center (str): label for top center of plot area
        label_top_left (str): label for top left of plot area
        label_top_right (str): label for top right of plot area
        orientation (str): orientation of figure, either "portrait" or
            "landscape"
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Define colors.
    color_count = len(arrays)
    if color_count == 1:
        colors_series = [colors["blue"]]
    elif color_count == 2:
        colors_series = [colors["gray"], colors["blue"]]
    elif color_count == 3:
        colors_series = [colors["gray"], colors["blue"], colors["orange"]]
    elif color_count > 3:
        colors_series = list(
            seaborn.color_palette("hls", n_colors=color_count)
        )
    # Create figure.
    if orientation == "portrait":
        figure = matplotlib.pyplot.figure(
            figsize=(11.811, 15.748),
            tight_layout=True
        )
    elif orientation == "landscape":
        figure = matplotlib.pyplot.figure(
            figsize=(15.748, 11.811),
            tight_layout=True
        )
    # Create axes.
    axes = matplotlib.pyplot.axes()
    # Create boxes.
    handle = axes.boxplot(
        arrays,
        notch=False,
        vert=True,
        widths=0.7,
        patch_artist=True,
        labels=labels_groups,
        manage_ticks=True,
    )
    # Fill boxes with colors.
    for box_patch, color_box in zip(handle["boxes"], colors_series):
        box_patch.set_facecolor(color_box)
        pass
    # Label axes.
    axes.set_ylabel(
        ylabel=label_vertical,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["two"]
    )
    if len(label_horizontal) > 0:
        axes.set_xlabel(
            xlabel=label_horizontal,
            labelpad=20,
            alpha=1.0,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"]["one"],
            rotation="horizontal",
        )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["two"]["size"],
        labelcolor=colors["black"]
    )
    if len(label_top_center) > 0:
        axes.text(
            0.5,
            0.9,
            label_top_center,
            horizontalalignment="center",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"]["one"]
        )
    if len(label_top_left) > 0:
        axes.text(
            0.25,
            0.9,
            label_top_left,
            horizontalalignment="center",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"]["two"]
        )
    if len(label_top_right) > 0:
        axes.text(
            0.75,
            0.9,
            label_top_right,
            horizontalalignment="center",
            verticalalignment="top",
            transform=axes.transAxes,
            backgroundcolor=colors["white"],
            color=colors["black"],
            fontproperties=fonts["properties"]["two"]
        )
    return figure


def plot_scatter_factor_groups(
    data=None,
    abscissa=None,
    ordinate=None,
    label_horizontal=None,
    label_vertical=None,
    factor=None,
    label_factor=None,
    labels_factors=None,
    fonts=None,
    colors=None,
    point_size=None,
    plot_factor_labels=None,
    legend=None,
):
    """
    Creates a figure of a chart of type scatter to represent the association
    of two variables.

    arguments:
        data (object): Pandas data frame of groups, series, and values
        abscissa (str): name of data column with variable for horizontal (x)
            axis
        ordinate (str): name of data column with variable for vertical (y) axis
        label_horizontal (str): label for horizontal axis
        label_vertical (str): label for vertical axis
        factor (str): name of data column with categorical variable to
            distinguish groups of instances
        label_factor (str): label to describe the factor
        labels_factors (list<str>): labels to describe the factor's values
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        point_size (float): size for scatter points
        plot_factor_labels (bool): whether to plot factor labels on chart
        legend (bool): whether to include a legend for series on the chart

    raises:

    returns:
        (object): figure object

    """

    ##########
    # Organize data.
    data = data.copy(deep=True)
    data.reset_index(
        level=None,
        inplace=True
    )
    data.set_index(
        factor,
        append=False,
        drop=True,
        inplace=True
    )
    groups = data.groupby(level=[factor])
    colors_series = list(seaborn.color_palette("hls", n_colors=len(groups)))

    ##########
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    # Create axes.
    axes = matplotlib.pyplot.axes()
    axes.set_xlabel(
        xlabel=label_horizontal,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.set_ylabel(
        ylabel=label_vertical,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["one"]["size"],
        labelcolor=colors["black"]
    )
    # Plot points for values from each group.
    index = 0
    for name, group in groups:
        values_x = group[abscissa].to_list()
        values_y = group[ordinate].to_list()
        handle = axes.plot(
            values_x,
            values_y,
            linestyle="",
            marker="o",
            markersize=point_size,
            markeredgecolor=colors_series[index],
            markerfacecolor=colors_series[index]
        )
        index += 1
        pass
    # Plot labels for each group.
    labels = []
    index = 0
    for name, group in groups:
        if plot_factor_labels:
            values_x = group[abscissa].to_list()
            mean_x = statistics.mean(values_x)
            values_y = group[ordinate].to_list()
            mean_y = statistics.mean(values_y)
            axes.text(
                mean_x,
                mean_y,
                str(index+1),
                backgroundcolor=colors["white_faint"],
                color=colors["black"],
                fontproperties=fonts["properties"]["three"],
                horizontalalignment="center",
                verticalalignment="center"
            )
        label = str(str(index+1) + ": " + str(labels_factors[index]))
        labels.append(label)
        index += 1
        pass
    # Create legend.
    # Create custome elements for the legend.
    if legend:
        elements = create_legend_elements(
            colors=colors_series,
            labels=labels
        )
        axes.legend(
            handles=elements,
            loc="upper right",
            prop=fonts["properties"]["four"],
            title=label_factor,
            title_fontsize=fonts["values"]["three"]["size"]
        )
    return figure


def plot_scatter(
    data=None,
    abscissa=None,
    ordinate=None,
    title_abscissa=None,
    title_ordinate=None,
    fonts=None,
    colors=None,
    size=None,
):
    """
    Creates a figure of a chart of type scatter.

    arguments:
        data (object): Pandas data frame of groups, series, and values
        abscissa (str): name of data column with variable for horizontal (x)
            axis
        ordinate (str): name of data column with variable for vertical (y) axis
        title_abscissa (str): title for abscissa on horizontal axis
        title_ordinate (str): title for ordinate on vertical axis
        factor (str): name of data column with groups or factors of samples
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties
        size (int): size of marker

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    data_copy = data.copy(deep=True)
    data_selection = data_copy.loc[:, [abscissa, ordinate]]
    data_selection.dropna(
        axis="index",
        how="any",
        inplace=True,
    )
    values_abscissa = data_selection[abscissa].values
    values_ordinate = data_selection[ordinate].values

    ##########
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    # Create axes.
    axes = matplotlib.pyplot.axes()
    axes.set_xlabel(
        xlabel=title_abscissa,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.set_ylabel(
        ylabel=title_ordinate,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["one"]["size"],
        labelcolor=colors["black"]
    )
    # Plot points for values from each group.
    handle = axes.plot(
        values_abscissa,
        values_ordinate,
        linestyle="",
        marker="o",
        markersize=size, # 5, 15
        markeredgecolor=colors["blue"],
        markerfacecolor=colors["blue"]
    )

    # Return figure.
    return figure

# TODO: probably obsolete?
def plot_scatter_threshold(
    data=None,
    abscissa=None,
    ordinate=None,
    threshold_abscissa=None,
    selection_abscissa=None,
    threshold_ordinate=None,
    selection_ordinate=None,
    title_abscissa=None,
    title_ordinate=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type scatter with thresholds on each
        dimension.

    arguments:
        data (object): Pandas data frame of groups, series, and values
        abscissa (str): name of data column with independent variable
        ordinate (str): name of data column with dependent variable
        threshold_abscissa (float): threshold for abscissa
        selection_abscissa (str): selection criterion for abscissa's values
            against threshold
        threshold_ordinate (float): threshold for ordinate
        selection_ordinate (str): selection criterion for ordinate's values
            against threshold
        title_abscissa (str): title for abscissa on horizontal axis
        title_ordinate (str): title for ordinate on vertical axis
        factor (str): name of data column with groups or factors of samples
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    data = data.copy(deep=True)
    data = data.loc[:, [abscissa, ordinate]]
    data.dropna(
        axis="index",
        how="any",
        inplace=True,
    )
    # Divide values by whether they pass thresholds on both dimensions.
    collection = utility.segregate_data_two_thresholds(
        data=data,
        abscissa=abscissa,
        ordinate=ordinate,
        threshold_abscissa=threshold_abscissa,
        selection_abscissa=selection_abscissa,
        threshold_ordinate=threshold_ordinate,
        selection_ordinate=selection_ordinate,
    )

    ##########
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    # Create axes.
    axes = matplotlib.pyplot.axes()
    axes.set_xlabel(
        xlabel=title_abscissa,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.set_ylabel(
        ylabel=title_ordinate,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["one"]["size"],
        labelcolor=colors["black"]
    )
    # Plot points for values from each group.
    handle = axes.plot(
        collection["fail"][abscissa].values,
        collection["fail"][ordinate].values,
        linestyle="",
        marker="o",
        markersize=2.5,
        markeredgecolor=colors["gray"],
        markerfacecolor=colors["gray"]
    )
    handle = axes.plot(
        collection["pass"][abscissa].values,
        collection["pass"][ordinate].values,
        linestyle="",
        marker="o",
        markersize=5,
        markeredgecolor=colors["blue"],
        markerfacecolor=colors["blue"]
    )

    # Plot lines for each threshold value...
    # Create lines for thresholds.
    axes.axvline(
        x=threshold_abscissa,
        ymin=0,
        ymax=1,
        alpha=1.0,
        color=colors["orange"],
        linestyle="--",
        linewidth=3.0,
    )
    axes.axhline(
        y=threshold_ordinate,
        xmin=0,
        xmax=1,
        alpha=1.0,
        color=colors["orange"],
        linestyle="--",
        linewidth=3.0,
    )

    # Return figure.
    return figure


def plot_scatter_label_emphasis_points(
    emphasis_keys=None,
    label_keys=None,
    column_key=None,
    column_label=None,
    line_abscissa=None,
    line_ordinate=None,
    line_ordinate_origin=None,
    data=None,
    abscissa=None,
    ordinate=None,
    title_abscissa=None,
    title_ordinate=None,
    fonts=None,
    colors=None,
):
    """
    Creates a figure of a chart of type scatter with thresholds on each
        dimension.

    arguments:
        emphasis_keys (list<str>): keys for rows of points for emphasis
        label_keys (list<str>): keys for rows of points for labels
        column_key (str): name of column in data with keys
        column_label (str): name of column in data with labels
        line_abscissa (float): point on abscissa for horizontal line
        line_ordinate (float): point on ordinate for vertical line
        line_ordinate_origin (bool): whether to draw vertical origin line
        data (object): Pandas data frame of groups, series, and values
        abscissa (str): name of data column with independent variable
        ordinate (str): name of data column with dependent variable
        title_abscissa (str): title for abscissa on horizontal axis
        title_ordinate (str): title for ordinate on vertical axis
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize data.
    data = data.copy(deep=True)
    ordinate_minimum = min(data[ordinate].to_list())
    ordinate_maximum = max(data[ordinate].to_list())
    data_bore = data.loc[~data[column_key].isin(emphasis_keys), :]
    data_emphasis = data.loc[data[column_key].isin(emphasis_keys), :]
    data_label = data.loc[data[column_key].isin(label_keys), :]
    data_bore.dropna(
        axis="index",
        how="any",
        inplace=True,
    )
    data_emphasis.dropna(
        axis="index",
        how="any",
        inplace=True,
    )
    data_label.dropna(
        axis="index",
        how="any",
        inplace=True,
    )

    ##########
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    # Create axes.
    axes = matplotlib.pyplot.axes()
    axes.set_xlabel(
        xlabel=title_abscissa,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.set_ylabel(
        ylabel=title_ordinate,
        labelpad=20,
        alpha=1.0,
        backgroundcolor=colors["white"],
        color=colors["black"],
        fontproperties=fonts["properties"]["one"]
    )
    axes.tick_params(
        axis="both",
        which="both",
        direction="out",
        length=5.0,
        width=3.0,
        color=colors["black"],
        pad=5,
        labelsize=fonts["values"]["one"]["size"],
        labelcolor=colors["black"]
    )
    # Plot points for values from each group.
    handle = axes.plot(
        data_bore[abscissa].to_numpy(),
        data_bore[ordinate].to_numpy(),
        linestyle="",
        marker="o",
        markersize=5,
        markeredgecolor=colors["gray"],
        markerfacecolor=colors["gray"]
    )
    handle = axes.plot(
        data_emphasis[abscissa].to_numpy(),
        data_emphasis[ordinate].to_numpy(),
        linestyle="",
        marker="o",
        markersize=7,
        markeredgecolor=colors["blue"],
        markerfacecolor=colors["blue"]
    )
    handle = axes.plot(
        data_label[abscissa].to_numpy(),
        data_label[ordinate].to_numpy(),
        linestyle="",
        marker="o",
        markersize=9,
        markeredgecolor=colors["orange"],
        markerfacecolor=colors["orange"]
    )

    # Plot lines for each threshold value...
    # Create lines for thresholds.
    if line_ordinate_origin:
        axes.axvline(
            x=0.0,
            ymin=0,
            ymax=1,
            alpha=1.0,
            color=colors["black"],
            linestyle="--",
            linewidth=3.0,
        )
    if line_abscissa is not None:
        axes.axvline(
            x=line_abscissa,
            ymin=0,
            ymax=1,
            alpha=1.0,
            color=colors["orange"],
            linestyle="--",
            linewidth=5.0,
        )
    if line_ordinate is not None:
        axes.axhline(
            y=line_ordinate,
            xmin=0,
            xmax=1,
            alpha=1.0,
            color=colors["orange"],
            linestyle="--",
            linewidth=5.0,
        )

    # Plot labels.
    # Place bottom of label above point by 5% of maximal y value.
    for label_key in label_keys:
        data_label = data.loc[data[column_key].isin([label_key]), :]
        if (data_label.shape[0] > 0):
            for index_point in data_label.index.to_list():
                axes.text(
                    (data_label.at[index_point, abscissa]),
                    (
                        data_label.at[index_point, ordinate] +
                        (0.02 * ordinate_maximum)
                    ),
                    data_label[column_label].to_list()[0],
                    backgroundcolor=colors["white_faint"],
                    color=colors["black"],
                    fontproperties=fonts["properties"]["three"],
                    horizontalalignment="center",
                    verticalalignment="bottom"
                )
                pass
            pass
        pass
    # Return figure.
    return figure


def create_legend_elements(
    colors=None,
    labels=None,
):
    """
    Creates custom elements for legend.

    arguments:
        colors (list<dict>): colors
        labels (str): name of data column with independent variable

    raises:

    returns:
        (list<object>): elements for legend

    """

    elements = []
    for index in range(len(labels)):
        element = matplotlib.lines.Line2D(
            [0],
            [0],
            marker="o",
            color=colors[index],
            label=labels[index],
            markerfacecolor=colors[index],
            markersize=15,
        )
        elements.append(element)
    return elements


def plot_overlap_sets(
    sets=None,
    fonts=None,
    colors=None,
):
    """
    Creates a Venn Diagram to represent overlap between multiple sets.

    arguments:
        sets (dict<list<str>>): values in sets
        fonts (dict<object>): references to definitions of font properties
        colors (dict<tuple>): references to definitions of color properties

    raises:

    returns:
        (object): figure object

    """

    # Organize information.
    names = list(sets.keys())
    # Create figure.
    figure = matplotlib.pyplot.figure(
        figsize=(15.748, 11.811),
        tight_layout=True
    )
    if len(names) == 2:
        venn = matplotlib_venn.venn2(
            subsets=[
                set(sets[names[0]]),
                set(sets[names[1]]),
            ],
            set_labels=names,
        )
    elif len(names) == 3:
        venn = matplotlib_venn.venn3(
            subsets=[
                set(sets[names[0]]),
                set(sets[names[1]]),
                set(sets[names[2]]),
            ],
            set_labels=names,
        )
    return figure


def write_figure(
    figure=None,
    format=None,
    resolution=None,
    path=None,
):
    """
    Writes figure to file.

    arguments:
        figure (object): figure object
        format (str): format suffix, "svg", "png"
        resolution (int): dots per inch (dpi) density for bitmap image, set to
            "None" with format "svg", otherwise "300" or "600"
        path (str): path to directory and file

    raises:

    returns:

    """

    # Write information to file.
    figure.savefig(
        path,
        format=format,
        dpi=resolution,
        facecolor="w",
        edgecolor="w",
        transparent=False
    )
    pass


# TODO: consider introducing a template set of functions... read, organize data, call appropriate plot function...

###############################################################################
# Procedure
# This module is not executable.
