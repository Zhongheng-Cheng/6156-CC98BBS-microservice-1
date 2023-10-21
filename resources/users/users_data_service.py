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