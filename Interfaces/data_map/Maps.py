import sys
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tüm Gatewayler')
        self.window_width, self.window_height = 1600, 1200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (41.046501460242084, 28.943273816048713)
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=12,
            location=coordinate
        )

        tooltip = "Ayrıntı için tıklayınız."
        folium.Marker(
            location=[41.046501460242084, 28.943273816048713],
            popup="<b>FSVMU Gateway</b>",
            tooltip=tooltip,
            icon = folium.Icon(color='red', icon='fa-wifi', prefix='fa'),
        ).add_to(m)

        folium.Marker(
            location=[41.08604679919651, 28.918229620197888],
            popup="<b>Ilhan Family Gateway</b>",
            tooltip=tooltip,
            icon = folium.Icon(color='red', icon='fa-wifi',prefix='fa'),
        ).add_to(m)

        folium.Marker(
            location=[41.038777, 28.951924],
            popup="<b>User Emre Tanrıverdi <br> [41.038777, 28.951924] </b>",
            tooltip=tooltip,
            icon=folium.Icon(color='blue', icon='fa-user', prefix='fa'),
        ).add_to(m)

        folium.Marker(
            location=[41.041901, 28.935599],
            popup="<b>User Emre Tanrıverdi <br> [41.04859602752246, 28.94236745160466] </b>",
            tooltip=tooltip,
            icon=folium.Icon(color='blue', icon='fa-user', prefix='fa'),
        ).add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        #---------------------------Markers-----------------------------------





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')


