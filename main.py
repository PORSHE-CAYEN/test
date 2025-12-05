from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0
        
        # Создаем вертикальный layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Создаем метку для отображения счетчика
        self.label = Label(
            text=f'Нажатий: {self.counter}',
            font_size=40
        )
        
        # Создаем кнопку
        self.button = Button(
            text='Нажми меня!',
            font_size=30,
            size_hint=(1, 0.5)
        )
        self.button.bind(on_press=self.increment_counter)
        
        # Добавляем виджеты в layout
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        
        return layout
    
    def increment_counter(self, instance):
        # Увеличиваем счетчик и обновляем текст
        self.counter += 1
        self.label.text = f'Нажатий: {self.counter}'

if __name__ == '__main__':
    CounterApp().run()