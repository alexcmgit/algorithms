<p><a href="https://www.beecrowd.com.br/repository/UOJ_2617_en.html">beecrowd.com.br/repository/UOJ_2617_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2617 </span>
                                    <h1>Provider Ajax SA</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>The financial sector has encountered some problems in the delivery of one of our providers, the delivery of the products does not match the invoice.</p>
                                    <p>Your job is to display the name of the products and the name of the provider, for the products supplied by the provider 'Ajax SA'.</p>
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
                      <td>Presidente Castelo Branco</td>
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
                      <td>South Chairs</td>
                      <td>Av Moinho</td>
                      <td>Santa Maria</td>
                      <td>RS</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Elon Electro</td>
                      <td>Apolo</td>
                      <td>São Paulo</td>
                      <td>SP</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Mike Electro</td>
                      <td>Pedro da Cunha</td>
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
                  <td><strong>value</strong></td>
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
                  <td>1</td>
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
                  <td>Blue Toaster</td>
                  <td>20</td>
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
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Red Chair</td>
          <td>Ajax SA</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>