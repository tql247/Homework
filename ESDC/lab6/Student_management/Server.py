from concurrent import futures
import logging

import grpc

import Student_management_pb2
import Student_management_pb2_grpc
from Student import Student
from Course import Course
from Reg import Reg


class Management(Student_management_pb2_grpc.ManagementServicer):
    ls_student = list()
    ls_course = list()
    ls_register = list()
    
    def create(self, request, context):
        cmd = request.req.split("-")
        if cmd[0] == "student":
            name = cmd[1]
            birth_year = int(cmd[2])
            gender = True
            if (cmd[3] == "False"):
                gender = False

            student = Student(name, birth_year, gender)
            student.push_id(len(self.ls_student))
            self.ls_student.append(student)
        else:
            name = cmd[1]
            credit = int(cmd[2])

            course = Course(name, credit)
            course.push_id(len(self.ls_course))
            self.ls_course.append(course)

        print("Create success!")
        return Student_management_pb2.Response(res='Create success!')

    def delete(self, request, context):
        cmd = request.req.split("-")

        if cmd[0] == "student":
            student_id = int(cmd[1])
            for student in self.ls_student:
                if student.get_id() == student_id:
                    self.ls_student.remove(student)
        else:
            course_id = int(cmd[1])
            for course in self.ls_course:
                if course.get_id() == course_id:
                    self.ls_course.remove(course)

        print("Delete success!")
        return Student_management_pb2.Response(res='Delete success!')

    def update(self, request, context):
        cmd = request.req.split("-")
        if cmd[0] == "student":
            student_id = int(cmd[1])
            name = cmd[2]
            birth_year = int(cmd[3])
            gender = True
            if (cmd[4] == "False"):
                gender = False


            for student in self.ls_student:
                if student.get_id() == student_id:
                    student.edit(name, birth_year, gender)
                    break
        else:
            course_id = int(cmd[1])
            name = cmd[2]
            credit = int(cmd[3])

            for course in self.ls_course:
                if course.get_id() == course_id:
                    course.edit(name, credit)

        print("Update success!")
        return Student_management_pb2.Response(res='Update success!')

    def register(self, request, context):
        cmd = request.req.split("-")
        student_id = int(cmd[0])
        course_id = int(cmd[1])

        student_idx = -1
        course_idx = -1

        for idx, student in enumerate(self.ls_student):
            if student.get_id() == student_id:
                student_idx = idx
                break

        for idx, course in enumerate(self.ls_course):
            if course.get_id() == course_id:
                course_idx = idx
                break
        
        reg = Reg(self.ls_student[student_idx], self.ls_course[course_idx])
        self.ls_register.append(reg)

        print("Register success!")
        return Student_management_pb2.Response(res='Register success!')

    def list(self, request, context):
        cmd = request.req.split("-")
        result=""


        if cmd[0] == "student":
            student_id = int(cmd[1])

            for reg in self.ls_register:
                if reg.get_student().get_id() == student_id:
                    result += "{" + reg.get_course().to_string() + "}"

        else:
            course_id = int(cmd[1])

            for reg in self.ls_register:
                if reg.get_course().get_id() == course_id:
                    result += "{" + reg.get_student().to_string() + "}"

        print("List success!")
        return Student_management_pb2.Response(res=result)
    
    def ls_all(self, request, context):
        result = ""

        if request.req == "student":
            for student in self.ls_student:
                result += "{" + student.to_string() + "}"

        else:
            for course in self.ls_course:
                result += "{" + course.to_string() + "}"

        print("List all success!")
        return Student_management_pb2.Response(res=result)

        
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Student_management_pb2_grpc.add_ManagementServicer_to_server(Management(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()