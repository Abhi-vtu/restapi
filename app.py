
from flask import Flask,jsonify

todo=Flask(__name__)

students=[
        {
            'id':1,
            'name':'std1',
            'age':21,
        },
        {
            'id':2,
            'name': 'std1',
            'age': 21,
        },
        {
            'id':3,
            'name': 'std1',
            'age': 21,
        }
    ]



@todo.route('/students-list')
def students_list():
   return jsonify(students)

@todo.route('/students/get/<int:id>')
def students_get_by_id(id):
    print(id)
    for std in students:
        if std['id']==id:
            return jsonify(std)
        print(std)
    return "i will return student"


if __name__ == "__main__":
        todo.run(
            debug=True
)

