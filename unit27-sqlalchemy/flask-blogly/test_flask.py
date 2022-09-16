from unittest import TestCase

import models
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.drop_all()
db.create_all()



class test_app(TestCase):

    def setUp(self):
        """gets rid of any users """
        Post.query.delete()
        User.query.delete()


    def tearDown(self):
        """clears db session """
        db.session.rollback()

    def test_show_users(self):
        """ Tests if all users show up on the users page """
        with app.test_client() as client:
            john = User(first_name='John',last_name='Doe')
            jane = User(first_name='Jane',last_name='Doe')
            mak = User(first_name='Mak',last_name='Klein')

            db.session.add(john)
            db.session.add(jane)
            db.session.add(mak)
            db.session.commit()

            res = client.get('/',follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertIn("John Doe",html)
            self.assertIn("Jane Doe",html)
            self.assertIn("Mak Klein",html)


    def test_user_page(self):
        """ Tests that the right user is shown on the user page """
        with app.test_client() as client:
            john = User(first_name='John',last_name='Doe')

            db.session.add(john)
            db.session.commit()

            res = client.get(f'/user/{john.id}')
            html = res.get_data(as_text=True)
            self.assertIn("John Doe",html)
            self.assertIn("Edit",html)
            self.assertIn("Delete",html)


    def test_delete_user(self):
        """ Tests if a user is deleted """
        with app.test_client() as client:
            john = User(first_name='John',last_name='Doe')

            db.session.add(john)
            db.session.commit()

            res = client.get(f'users/{john.id}/delete',follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertNotIn("John Doe",html)


    def test_post_page(self):
        """ Tests that the right post is shown """
        with app.test_client() as client:

            john = User(first_name='John',last_name='Doe')
            db.session.add(john)
            db.session.commit()


            new_post = Post(title='testPost',content='this is a test post',user_id=john.id)

            db.session.add(new_post)
            db.session.commit()

            res = client.get(f'/posts/{new_post.id}')
            html = res.get_data(as_text=True)
            self.assertIn("testPost",html)
            self.assertIn("this is a test post",html)
            self.assertIn("Edit",html)
            self.assertIn("Delete",html)



    def test_add_post(self):
        """ Tests if a new post is added """
        with app.test_client() as client:
            john = User(first_name='John',last_name='Doe')
            db.session.add(john)
            db.session.commit()
            res = client.post(f'/users/{john.id}/posts/new',data={'title':'test2','content':'this is also a test'},follow_redirects=True)
            html = res.get_data(as_text = True)
            self.assertIn("test2",html)




    def test_edit_post(self):
            """ Tests if a post is edited """
            with app.test_client() as client:
                john = User(first_name='John',last_name='Doe')
                db.session.add(john)
                db.session.commit()


                new_post = Post(title='testPost',content='this is a test post',user_id=rose.id)
                db.session.add(new_post)
                db.session.commit()


                res = client.post(f'/posts/{new_post.id}/edit',data={'title':'testPost','content':'this is an edited post'},follow_redirects=True)
                html = res.get_data(as_text = True)
                self.assertIn("this is an edited post",html)