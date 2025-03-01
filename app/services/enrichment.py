import csv
import io

import aiohttp


class Enrichment:

    async def process(self, patient_data_url: str, enrichment_data_url: str):
        """

        :param patient_data_url:
        :param enrichment_data_url:
        :return:
        """
        patient_data = await self.__download_csv(patient_data_url)
        enrichment_data = await self.__download_csv(enrichment_data_url)

        response = await self.enrich_data(patient_data=patient_data, enrichment_data=enrichment_data)
        await self.__write_data_to_csv(data=response)
        return response

    @staticmethod
    async def __download_csv(url: str) -> list[dict]:
        """

        :param url:
        :return:
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                csv_text = await response.text()
                str_file = io.StringIO(csv_text, newline='\n')
                reader = csv.DictReader(str_file)
                data = [line for line in reader]
                return data

    @staticmethod
    async def __write_data_to_csv(*, data: list[dict], file_path: str = "output.csv", ):
        """

        :param file_path:
        :return:
        """
        keys = data[0].keys()
        with open(file_path, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    @staticmethod
    async def enrich_data(*, patient_data: list[dict], enrichment_data: list[dict]):
        """

        :param patient_data:
        :param enrichment_data:
        :return:
        """
        output = []
        for patient in patient_data:
            for enrichment in enrichment_data:
                if (
                        patient["chromosome"] == enrichment["chromosome"] and
                        patient["position"] == enrichment["position"] and
                        patient["ref"] == enrichment["ref"] and
                        patient["alt"] == enrichment["alt"]
                ):
                    patient["info"] = enrichment["info"]
                    output.append(patient)
                    break
            else:
                patient["info"] = None
                output.append(patient)
        return output
