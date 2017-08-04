'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''


def analog_clock_factory():
    from .android_analog_clock import AndroidAnalogClock
    return AndroidAnalogClock


def auto_complete_text_view_factory():
    from .android_auto_complete_text_view import AndroidAutoCompleteTextView
    return AndroidAutoCompleteTextView


def button_factory():
    # print "Import button"
    from .android_button import AndroidButton
    return AndroidButton


def calendar_view_factory():
    # print "Import calendar view"
    from .android_calendar_view import AndroidCalendarView
    return AndroidCalendarView


def card_view_factory():
    # print "Import card view"
    from .android_card_view import AndroidCardView
    return AndroidCardView


def checkbox_factory():
    # print "Import checkbox"
    from .android_checkbox import AndroidCheckBox
    return AndroidCheckBox


def chronometer_factory():
    # print "Import chronometer"
    from .android_chronometer import AndroidChronometer
    return AndroidChronometer


def compound_button_factory():
    # print "Import compound button"
    from .android_compound_button import AndroidCompoundButton
    return AndroidCompoundButton


def date_picker_factory():
    # print "Import date picker"
    from .android_date_picker import AndroidDatePicker
    return AndroidDatePicker


def drawer_layout_factory():
    # print "Import drawer layout"
    from .android_drawer_layout import AndroidDrawerLayout
    return AndroidDrawerLayout


def edit_text_factory():
    # print "Import edit text"
    from .android_edit_text import AndroidEditText
    return AndroidEditText


def fragment_factory():
    # print "Import frame layout"
    from .android_fragment import AndroidFragment
    return AndroidFragment


def frame_layout_factory():
    # print "Import frame layout"
    from .android_frame_layout import AndroidFrameLayout
    return AndroidFrameLayout


def grid_layout_factory():
    # print "Import grid layout"
    from .android_grid_layout import AndroidGridLayout
    return AndroidGridLayout


def icon_factory():
    from .android_iconify import AndroidIcon
    return AndroidIcon


def icon_button_factory():
    from .android_iconify import AndroidIconButton
    return AndroidIconButton


def icon_toggle_button_factory():
    from .android_iconify import AndroidIconToggleButton
    return AndroidIconToggleButton


def image_view_factory():
    from .android_image_view import AndroidImageView
    return AndroidImageView


def linear_layout_factory():
    # print "Import linear layout"
    from .android_linear_layout import AndroidLinearLayout
    return AndroidLinearLayout


def list_item_factory():
    # print "Import linear layout"
    from .android_list_view import AndroidListItem
    return AndroidListItem


def list_view_factory():
    # print "Import linear layout"
    from .android_list_view import AndroidListView
    return AndroidListView


def number_picker_factory():
    # print "Import view"
    from .android_number_picker import AndroidNumberPicker
    return AndroidNumberPicker


def pager_title_strip_factory():
    from .android_view_pager import AndroidPagerTitleStrip
    return AndroidPagerTitleStrip


def pager_tab_strip_factory():
    from .android_view_pager import AndroidPagerTabStrip
    return AndroidPagerTabStrip


def pager_fragment_factory():
    from .android_fragment import AndroidPagerFragment
    return AndroidPagerFragment


def progress_bar_factory():
    # print "Import progress bar"
    from .android_progress_bar import AndroidProgressBar
    return AndroidProgressBar


def radio_button_factory():
    # print "Import radio button"
    from .android_radio_button import AndroidRadioButton
    return AndroidRadioButton


def radio_group_factory():
    # print "Import radio group"
    from .android_radio_group import AndroidRadioGroup
    return AndroidRadioGroup


def rating_bar_factory():
    # print "Import rating bar"
    from .android_rating_bar import AndroidRatingBar
    return AndroidRatingBar


def relative_layout_factory():
    # print "Import relative layout"
    from .android_relative_layout import AndroidRelativeLayout
    return AndroidRelativeLayout


def scroll_view_factory():
    # print "Import scroll view"
    from .android_scroll_view import AndroidScrollView
    return AndroidScrollView


def seek_bar_factory():
    from .android_seek_bar import AndroidSeekBar
    return AndroidSeekBar


def spacer_factory():
    # print "Import switch"
    from .android_spacer import AndroidSpacer
    return AndroidSpacer


def spinner_factory():
    # print "Import spinner"
    from .android_spinner import AndroidSpinner
    return AndroidSpinner


def switch_factory():
    # print "Import switch"
    from .android_switch import AndroidSwitch
    return AndroidSwitch


def text_clock_factory():
    from .android_text_clock import AndroidTextClock
    return AndroidTextClock


def text_view_factory():
    # print "Import text view"
    from .android_text_view import AndroidTextView
    return AndroidTextView


def time_picker_factory():
    # print "Import time picker"
    from .android_time_picker import AndroidTimePicker
    return AndroidTimePicker


def tab_layout_factory():
    # print "Import tab host"
    from .android_tab_layout import AndroidTabLayout
    return AndroidTabLayout


def tab_fragment_factory():
    # print "Import tab host"
    from .android_tab_layout import AndroidTabFragment
    return AndroidTabFragment


def toggle_button_factory():
    # print "Import toggle button"
    from .android_toggle_button import AndroidToggleButton
    return AndroidToggleButton


def toolbar_factory():
    from .android_toolbar import AndroidToolbar
    return AndroidToolbar


def view_factory():
    # print "Import view"
    from .android_view import AndroidView
    return AndroidView


def view_group_factory():
    # print "Import view group"
    from .android_view_group import AndroidViewGroup
    return AndroidViewGroup


def view_pager_factory():
    # print "Import view pager"
    from .android_view_pager import AndroidViewPager
    return AndroidViewPager


def web_view_factory():
    from .android_web_view import AndroidWebView
    return AndroidWebView


IOS_FACTORIES = {
    'AnalogClock': analog_clock_factory,
    'AutoCompleteTextView': auto_complete_text_view_factory,
    'Button': button_factory,
    'CalendarView': calendar_view_factory,
    'CardView': card_view_factory,
    'CheckBox': checkbox_factory,
    'Chronometer': chronometer_factory,
    'CompoundButton': compound_button_factory,
    'DatePicker': date_picker_factory,
    'DrawerLayout': drawer_layout_factory,
    'EditText': edit_text_factory,
    'Fragment': fragment_factory,
    'FrameLayout': frame_layout_factory,
    'GridLayout': grid_layout_factory,
    'Icon': icon_factory,
    'IconButton': icon_button_factory,
    'IconToggleButton': icon_toggle_button_factory,
    'ImageView': image_view_factory,
    'LinearLayout': linear_layout_factory,
    'ListItem': list_item_factory,
    'ListView': list_view_factory,
    'NumberPicker': number_picker_factory,
    'PagerTitleStrip': pager_title_strip_factory,
    'PagerTabStrip': pager_tab_strip_factory,
    'PagerFragment': pager_fragment_factory,
    'ProgressBar': progress_bar_factory,
    'RadioButton': radio_button_factory,
    'RadioGroup': radio_group_factory,
    'RatingBar': rating_bar_factory,
    'RelativeLayout': relative_layout_factory,
    'ScrollView': scroll_view_factory,
    'SeekBar': seek_bar_factory,
    'Spacer': spacer_factory,
    'Spinner': spinner_factory,
    'Switch': switch_factory,
    'TabFragment': tab_fragment_factory,
    'TabLayout': tab_layout_factory,
    'TextClock': text_clock_factory,
    'TextView': text_view_factory,
    'TimePicker': time_picker_factory,
    'ToggleButton': toggle_button_factory,
    'Toolbar': toolbar_factory,
    'View': view_factory,
    'ViewGroup': view_group_factory,
    'ViewPager': view_pager_factory,
    'WebView': web_view_factory,
}