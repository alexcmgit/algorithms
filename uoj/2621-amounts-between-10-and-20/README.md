<p><a href="https://www.beecrowd.com.br/repository/UOJ_2621_en.html">beecrowd.com.br/repository/UOJ_2621_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2621 </span>
                                    <h1>Amounts Between 10 and 20</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>When it comes to delivering the report on how many products the company has in stock, a part of the report has become corrupted, so the stock keeper asked for help, he wants you to display the following data for him.</p>
                                    <p>Display the name of products whose amount are between 10 and 20 and whose name of the supplier starts with the letter 'P'.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>providers</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>street</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>city</td>
                                  <td>character varying (255)</td>
                                </tr>
                                <tr>
                                  <td>state</td>
                                  <td>char (2)</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>products</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>name</td>
                              <td>character varying (255)</td>
                            </tr>
                            <tr>
                              <td>amount</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>price</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>id_providers (FK)</td>
                              <td>numeric</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>providers</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>street</strong></td>
                      <td><strong>city</strong></td>
                      <td><strong>state</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Ajax SA</td>
                      <td>Rua Presidente Castelo Branco</td>
                      <td>Porto Alegre</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Sansul SA</td>
                      <td>Av Brasil</td>
                      <td>Rio de Janeiro</td>
                      <td>RJ</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Pr Sheppard Chairs</td>
                      <td>Rua do Moinho</td>
                      <td>Santa Maria</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Elon Electro</td>
                      <td>Rua Apolo</td>
                      <td>São Paulo</td>
                      <td>SP</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Mike Electro</td>
                      <td>Rua Pedro da Cunha</td>
                      <td>Curitiba</td>
                      <td>PR</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>products</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>amount</strong></td>
                  <td><strong>price</strong></td>
                  <td><strong>id_providers</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Blue Chair</td>
                  <td>30</td>
                  <td>300.00</td>
                  <td>5</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Red Chair</td>
                  <td>50</td>
                  <td>2150.00</td>
                  <td>2</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Disney Wardrobe</td>
                  <td>400</td>
                  <td>829.50</td>
                  <td>4</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Executive Chair</td>
                  <td>17</td>
                  <td>9.90</td>
                  <td>3</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Solar Panel</td>
                  <td>30</td>
                  <td>3000.25</td>
                  <td>4</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Executive Chair</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>