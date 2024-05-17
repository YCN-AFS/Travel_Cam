# import re
#
# original_string = "map_0/Layer_1.png"
# desired_number = 42
#
# # Replace the pattern "_\d+" (underscore followed by one or more digits)
# # with the desired number
# new_string = re.sub(r"Layer_\d+", f"Layer_{desired_number}", original_string)
#
# print(new_string)  # Output: map_42/Layer 1.png

# import os
#
# # Thay đổi đường dẫn thư mục theo ý muốn
# directory = "assets/background/map_0"
#
# # Lấy danh sách các tệp trong thư mục
# files = os.listdir(directory)
# print(files)
#
# # In tên của mỗi tệp
# for file in files:
#     print(file)


# class Animal:
#     def __init__(self):
#         self.name = "Fox"
#         self.color = "red"
#     def changeColor(self):
#         self.color = "Blue"
#
# class Pet(Animal):
#     def __init__(self):
#         super().__init__()  # Gọi phương thức khởi tạo của lớp cha
#         # Cài đặt các thuộc tính khác của lớp Pet (nếu cần)
#
# # Tạo một đối tượng Pet
# my_pet = Pet()
# print(f"Tên của thú cưng là {my_pet.name}")
# print(f"Màu lông của thú cưng là {my_pet.color}")


# class Animal:
#     def __init__(self):
#         self.name = "Fox"
#         self.color = "red"
#
# class Pet(Animal):
#     def __init__(self):
#         super().__init__()  # Gọi phương thức khởi tạo của lớp cha
#         self.name = "Dog"  # Ghi đè thuộc tính name của lớp Animal
#         def over_write(self):
#             super().__init__()
#             self.color = "Blue"
#
# # Tạo một đối tượng Pet
# my_pet = Pet()
# print(f"Tên của thú cưng là {my_pet.name}")  # In ra "Dog"
# print(f"Màu lông của thú cưng là {my_pet.color}")  # In ra "red"

# class Animal:
#     def __init__(self):
#         self.name = "Fox"
#         self.color = "red"
#
# class Pet(Animal):
#     def __init__(self):
#         super().__init__()  # Gọi phương thức khởi tạo của lớp cha
#         self.name = "Dog"  # Ghi đè thuộc tính name của lớp Animal
#
#     def over_write(self):
#         super().__init__()
#         self.color = "Blue"
#
# # Tạo một đối tượng Pet
# my_pet = Pet()
# print(f"Tên của thú cưng là {my_pet.name}")
# print(f"Màu lông của thú cưng là {my_pet.color}")
#
# # Gọi phương thức over_write
# my_pet.over_write()
# print(f"Màu lông của thú cưng sau khi gọi phương thức over_write là {my_pet.color}")

import mediapipe as mp

# Initialize the Holistic solution
mp_holistic = mp.solutions.holistic.Holistic()

# Set the GPU options
mp.start_run(options=[mp.gpu.get_gpu_options()])

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    success, image = cap.read()
    if not success:
        break

    # Process the image with MediaPipe
    results = mp_holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Display the processed image or perform further processing as needed
    cv2.imshow('MediaPipe Holistic', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()