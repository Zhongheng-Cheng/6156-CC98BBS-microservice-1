from resources.abstract_base_data_service import BaseDataService
import json


class UserDataService(BaseDataService):

    def __init__(self, config: dict):
        """

        :param config: A dictionary of configuration parameters.
        """
        super().__init__()

        self.data_dir = config['data_directory']
        self.data_file = config["data_file"]
        self.users = []

        self._load()

    def _get_data_file_name(self):
        # DFF TODO Using os.path is better than string concat
        result = self.data_dir + "/" + self.data_file
        return result

    def _load(self):
        fn = self._get_data_file_name()
        with open(fn, "r") as in_file:
            self.users = json.load(in_file)

    def _save(self):
        fn = self._get_data_file_name()
        with open(fn, "w") as out_file:
            json.dump(self.users, out_file)

    def get_users(self, 
                  user_id: str = None, 
                  user_name: str = None, 
                  password: str = None,
                  email: str = None,
                  profile_picture: str = None,
                  role: str = None
                  ) -> list:
        """

        Returns users with properties matching the values. Only non-None parameters apply to
        the filtering.

        :param user_id: user_id to match.
        :param user_name: user_name to match.
        :param password: password to match.
        :param email: email to match.
        :param profile_picture: profile_picture to match.
        :param role: role to match.
        :return: A list of matching JSON records.
        """
        result = []
        
        for s in self.users:

            if (user_id is None or (s.get("user_id", None) == user_id)) and \
                    (user_name is None or (s.get("user_name", None) == user_name)) and \
                    (password is None or (s.get("password", None) == password)) and \
                    (email is None or (s.get("email", None) == email)) and \
                    (profile_picture is None or (s.get("profile_picture", None) == profile_picture)) and \
                    (role is None or (s.get("role", None) == role)):
                result.append(s)

        return result
    
    def create_user(self, 
                  user_id: str = None, 
                  user_name: str = None, 
                  password: str = None,
                  email: str = None,
                  profile_picture: str = None,
                  role: str = None
                  ):
        if not profile_picture:
            profile_picture = '1'
        if not role:
            role = 'Student'
        if user_id in [user['user_id'] for user in self.users]:
            print(f"user_id: {user_id} already exists")
            return
        self.users.append({
            "user_id": user_id,
            "user_name": user_name,
            "password": password,
            "email": email,
            "profile_picture": profile_picture,
            "role": role
        })
        print("======================")
        print(self.users)
        print("======================")
        self._save()
        return
    
    def update_user(self, **args):
        if 'user_id' in args.keys():
            for user in self.users:
                if user['user_id'] == args['user_id']:
                    for i in args.items():
                        if i[0] in ['user_id', 'user_name', 'password', 'email', 'profile_picture', 'role']:
                            user[i[0]] = i[1]
        self._save()
        return
    
    def delete_user(self, **args):
        for user in self.users:
            is_target_user = True
            for i in args.items():
                if user[i[0]] != i[1]:
                    print('None')
                    is_target_user = False
            if is_target_user:
                print(user)
                tmp = self.users.index(user)
                print(tmp)
                self.users.pop(tmp)
        self._save()
        return